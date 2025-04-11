import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import openai

def analyze_sentiment_with_ai(text):
    """Анализ тематики текста с помощью OpenAI"""
    prompt = f"Проанализируй текст песни и определи его основную тематику (любовь, грусть, природа, путешествия и т.д.). Ответь кратко, 3-5 ключевых тем.\n\nТекст: {text[:3000]}\n\nТемы:"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты опытный лингвист и музыкальный критик."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Ошибка AI анализа: {e}")
        return "Не удалось определить тематику"

def process_text(text):
    """Обработка текста и генерация статистики"""
    words = re.split(r'[ ,.!?\n]+', text)
    words_lower = [word.lower() for word in words if word and len(word) > 2]
    words_counts = Counter(words_lower)
    return words_lower, words_counts

def main():
    print("Введите текст песни (для завершения нажмите Enter дважды):")
    text_input = []
    while True:
        line = input()
        if line:
            text_input.append(line)
        else:
            break
    
    text = "\n".join(text_input)
    if not text:
        print("Текст не введен!")
        return
    
    # Анализ тематики с помощью AI
    print("\n🔍 Анализ тематики текста...")
    themes = analyze_sentiment_with_ai(text)
    print("\n🎵 Основные темы песни:")
    print(themes)
    
    # Статистика по словам
    words_lower, words_counts = process_text(text)
    
    print("\n📊 Статистика слов:")
    for word, count in words_counts.most_common(15):  # Топ-15 слов
        print(f"{word}: {count}")
    
    print(f"\n📌 Всего уникальных слов: {len(words_counts)}")
    print(f"📌 Всего слов: {sum(words_counts.values())}")
    
    # Облако слов
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='plasma',
        max_words=100
    ).generate_from_frequencies(words_counts)
    
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Облако слов из текста песни", pad=20)
    plt.show()

if __name__ == "__main__":
    # Установите ваш API-ключ OpenAI
    openai.api_key = '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' 
    main()