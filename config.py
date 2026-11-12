"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY ARABIC"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "ARABIC"
HANDLE = "@velocityarabic"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'ar',
 'name': 'Arabic',
 'native_name': 'العربية',
 'history_key': 'arabic',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'ar-SA-ZariyahNeural',
 'native_fallback_voice': 'ar-SA-HamedNeural',
 'native_engine': 'edge',
 'native_lang_code': 'ar',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'العربية',
 'translit_label': 'SAY IT LIKE',
 'flag': 'sa',
 'greeting': 'مرحباً!',
 'encouragement': 'ممتاز!',
 'rtl': True,
 'char_tiles': False,
 'script_font': 'Script.ttf',
 'glyphs': 'أبتثجحخدذرزسشصضطظعغفقكلمنهوي'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'تحفيز',
 'Love': 'حب',
 'Success': 'نجاح',
 'Wisdom': 'حكمة',
 'Happiness': 'سعادة',
 'Self Improvement': 'تطوير الذات',
 'Gratitude': 'امتنان',
 'Friendship': 'صداقة',
 'Hope': 'أمل',
 'Creativity': 'إبداع',
 'Inner Peace': 'سلام داخلي',
 'Confidence': 'ثقة',
 'Perseverance': 'مثابرة',
 'Inspiration': 'إلهام',
 'Positive Life': 'حياة إيجابية',
 'Courage': 'شجاعة',
 'Kindness': 'لطف',
 'Patience': 'صبر',
 'Forgiveness': 'غفران',
 'Strength': 'قوة',
 'Joy': 'فرح',
 'Balance': 'توازن',
 'Growth': 'نمو',
 'Purpose': 'هدف',
 'Mindfulness': 'وعي ذهني',
 'Travel & Airport': 'السفر والمطار',
 'Ordering Food & Dining': 'طلب الطعام وتناول الطعام',
 'Shopping & Prices': 'التسوق والأسعار',
 'Asking for Directions': 'طلب الاتجاهات',
 'Hotel & Accommodation': 'الفنادق والإقامة',
 'Daily Routine': 'الروتين اليومي',
 'Meeting People & Greetings': 'مقابلة الناس والتحيات',
 'Emergency & Health': 'الطوارئ والصحة',
 'Public Transportation': 'المواصلات العامة',
 'Work & Office': 'العمل والمكتب',
 'Weather & Small Talk': 'الطقس والأحاديث العابرة',
 'Coffee Shop & Bakery': 'المقهى والمخبز',
 'Family & Home': 'العائلة والمنزل',
 'Hobbies & Free Time': 'الهوايات ووقت الفراغ',
 'Dating & Romance': 'المواعدة والرومانسية',
 'Phone Calls & Messages': 'المكالمات الهاتفية والرسائل',
 'Banking & Money': 'البنوك والمال',
 'Doctor & Pharmacy': 'الطبيب والصيدلية',
 'Sports & Fitness': 'الرياضة واللياقة البدنية',
 'Celebrations & Parties': 'الاحتفالات والحفلات',
 'Feelings & Emotions': 'المشاعر والأحاسيس',
 'Agreeing & Disagreeing': 'الموافقة والاختلاف',
 'Making Plans': 'وضع الخطط',
 'Common Native Slang': 'العامية المحلية الشائعة',
 'Cultural Traditions': 'التقاليد الثقافية'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnarabic',
 '#arabiclessons',
 '#arabicforbeginners',
 '#languagelearning',
 '#arabicvocabulary',
 '#velocityarabic',
 '#dailyarabic',
 '#arabic',
 '#learnlanguages',
 '#speakarabic']
# ==== HASHTAGS END ====
