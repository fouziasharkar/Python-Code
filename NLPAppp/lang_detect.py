from langdetect import detect_langs, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Optional: set a seed to make language detection more deterministic
DetectorFactory.seed = 0

# Mapping from language codes to full language names
lang_map = {
    'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'ca': 'Catalan',
    'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'el': 'Greek',
    'en': 'English', 'es': 'Spanish', 'et': 'Estonian', 'fa': 'Persian', 'fi': 'Finnish',
    'fr': 'French', 'gu': 'Gujarati', 'he': 'Hebrew', 'hi': 'Hindi', 'hr': 'Croatian',
    'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
    'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam',
    'mr': 'Marathi', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pa': 'Punjabi',
    'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sk': 'Slovak',
    'sl': 'Slovenian', 'so': 'Somali', 'sq': 'Albanian', 'sv': 'Swedish', 'sw': 'Swahili',
    'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Tagalog', 'tr': 'Turkish',
    'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)'
}


def detect_languages_with_scores(text):
    try:
        # Detect languages with scores for the entire text
        results = detect_langs(text)

        detected_languages = []
        for result in results:
            lang_code = result.lang
            lang_name = lang_map.get(lang_code, 'Unknown')
            confidence_score = result.prob

            detected_languages.append((lang_name, confidence_score))

        return detected_languages

    except LangDetectException as e:
        print("Error:", e)
        return [('Unknown', 0.0)]


# Example usage:
if __name__ == "__main__":
    text = "John Doe has been working for Microsoft in Seattle since 1999. Et il parle aussi un peu français."
    detected_languages = detect_languages_with_scores(text)

    print("Detected languages with scores:")
    for lang, score in detected_languages:
        print(f"{lang}: {score}")
