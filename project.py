import re
from collections import Counter 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tkinter as tk
from tkinterdnd2 import TkinterDnD 

class textAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Анализатор текста")
        self.root.geometry("600x400")
            
        self.textBox = tk.Text(root, wrap=tk.WORD, width=70, height=20)
        self.textBox.pack(pady=10)
        self.textBox.drop_target_register('DND_Files')
        self.textBox.dnd_bind('<<Drop>>', self.fileInput)
        self.textBox.insert(tk.END, "Перетащите файл .txt")
            
        self.analyzeButton = tk.Button(root, text="Анализировать", state=tk.ACTIVE, command=self.textAnalyseOutput)
        self.analyzeButton.pack()
            
        self.wordsLower = []
        self.wordsCounts = Counter()
        self.stopWords = [
            'и', 'в', 'во', 'на', 'с', 'по', 'к', 'у', 'о',
            'из', 'за', 'от', 'для', 'не', 'то', 'же', 'бы',
            'это', 'как', 'а', 'но', 'да', 'нет', 'так', 'я',
            '—', 'что', "(", ")", "ты:", "мне", "все", "вам",
            "вас", "ну", "ах", "ли", "ж", "со", "их", "уж",
            "ей", "ни", "где", "чтоб", "вот", "вы", "ты", "где",
            "до"
        ]

    def fileInput(self, event):
        filePath = event.data.strip("{}")
        if filePath.endswith(".txt"):
            try:
                with open(filePath, "r") as f:
                    text = f.read()
                self.textBox.delete('1.0', tk.END)
                self.textBox.insert(tk.END, text)
                self.analyzeButton.config(state=tk.NORMAL)
            except Exception as e:
                self.textBox.delete('1.0', tk.END)
                self.textBox.insert(tk.END, f"Ошибка: {str(e)}")
        else:
            self.textBox.delete('1.0', tk.END)
            self.textBox.insert(tk.END, "Перетащите файл .txt")

    def processText(self, text):
        words = re.split(r'[ ,.!?\n]+', text)
        wordsLower = [word.lower() for word in words]
        wordsLower = [word for word in wordsLower if word not in self.stopWords]
        wordsCounts = Counter(wordsLower)
        return wordsLower, wordsCounts
    
    def textAnalyseOutput(self):
        text = self.textBox.get("1.0", tk.END)
        if not text.strip():
            return

        self.wordsLower, self.wordsCounts = self.processText(text)
       
        for word ,count in self.wordsCounts.most_common(100):
            print(f"{word}: {count}")
        print("All unique words ", len(self.wordsCounts))
        #print("Array of words", self.wordsLower)

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(self.wordsCounts)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

root = TkinterDnD.Tk()
app = textAnalyzer(root)
root.mainloop()

#pip install wordcloud matplotlib numpy pillow