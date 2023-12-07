import requests
from concurrent.futures import ThreadPoolExecutor
from nltk.corpus import stopwords
from pymystem3 import Mystem
import gensim
from gensim import corpora
from pyrogram import Client
import tkinter as tk


class DataParser:
    def __init__(self):
        self.mystem = Mystem()
        self.russian_stopwords = set(stopwords.words("russian"))

    def telegram(self):
        api = ''
        hash_key = ''
        phone = ''
        channels = []
        result = []
        with open('telegram.txt') as file:
            channels.append(file.readline().strip())

        with Client(phone, api, hash_key) as client:
            for id in channels:
                channel_info = client.get_chat(id)
                posts = client.get_chat_history(channel_info.id, limit=100)
                for x in posts: result.append(x.caption)
        return result

    def vk(self):
        api = ''
        version = 5.131
        amount = 100
        channels = []
        result = []
        with open('vk.txt') as file:
            channels.append(file.readline().strip())

        for id in channels:
            response = requests.get(
                'https://api.vk.com/method/wall.get',
                params={'access_token': api, 'v': version, 'owner_id': int(id), 'count': amount}
            ).json()

            for i in range(amount):
                result.append(response['response']['items'][i]['text'])
        return result


class TextProcessor:
    def __init__(self, mystem, russian_stopwords):
        self.mystem = mystem
        self.russian_stopwords = russian_stopwords

    def get_words(self, text):
        words = self.mystem.lemmatize(text.lower())
        result = [word for word in words if word not in self.russian_stopwords and token != " "]
        text = ' '.join(result)
        return text


class TopicModeler:
    def getWeights(self, lines):
        dictionary = corpora.Dictionary([x.split() for x in lines])

        model = gensim.models.LdaModel
        lda_model = model(id2word=dictionary, num_topics=5, passes=50)

        return lda_model.print_topics(num_topics=3, num_words=4)


class ProgramInterface(tk.Tk):
    def __init__(self, data_parser, text_processor, topic_modeler):
        super().__init__()
        self.title("Text Processing App")
        self.geometry("800x600")
        self.data_parser = data_parser
        self.text_processor = text_processor
        self.topic_modeler = topic_modeler

        self.create_widgets()

    def create_widgets(self):
        self.main_label = tk.Label(self, text="Text Processing App", font=("Helvetica", 16))
        self.main_label.pack(pady=20)

        self.process_button = tk.Button(self, text="Запуск программы", command=self.parsing)
        self.process_button.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

    def parsing(self):
        self.result_label.config(text="Processing... Please wait.")

        with ThreadPoolExecutor() as executor:
            vk_result, tg_result = executor.submit(self.data_parser.vk), executor.submit(
                self.data_parser.telegram)

        with ThreadPoolExecutor() as executor:
            processed_data_parallel_vk = list(executor.map(self.text_processor.get_tokens, vk_result.result()))
            processed_data_parallel_tg = list(executor.map(self.text_processor.get_tokens, tg_result.result()))

        vk_results = self.topic_modeler.getWeights(processed_data_parallel_vk)
        tg_results = self.topic_modeler.getWeights(processed_data_parallel_tg)

        result_text = f"VK themes:\n{vk_results}\n\nTelegram themes:\n{tg_results}"

        with open('vk_results.txt', 'a') as topics_vk:
            for topic in vk_results:
                topics_vk.write(str(topic) + '\n')

        with open('telegram_results.txt', 'a') as topics_tg:
            for topic in tg_results:
                topics_tg.write(str(topic) + '\n')

        self.result_label.config(text=result_text)


if __name__ == '__main__':
    data_parser = DataParser()
    text_processor = TextProcessor(data_parser.mystem, data_parser.russian_stopwords)
    topic_modeler = TopicModeler()

    program_interface = ProgramInterface(data_parser, text_processor, topic_modeler)
    program_interface.mainloop()
