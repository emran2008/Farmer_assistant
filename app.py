from flask import Flask, request, render_template, jsonify
from flask import Flask, render_template
from flask import Flask, render_template, request
from pathlib import Path
import sys
import sys
import os
import pandas as pd

BIOFLOC_CALCULATOR_DIR = (
    Path(__file__).resolve().parent
    / "Aquaculture System"
    / "Biofloc"
    / "Biofloc Calculator"
)
sys.path.insert(0, str(BIOFLOC_CALCULATOR_DIR))

from biofloc_calculator import calculate_biofloc

POND_MODEL_DIR = Path(__file__).resolve().parent / "Aquaculture System" / "Pond Culture" / "Pond ML Model"

sys.path.insert(0, str(POND_MODEL_DIR))

from pond_predictor import predict_fish
from weather import get_weather
import numpy as np
import pandas
import requests
from datetime import date, timedelta
import sklearn
import pickle
import sqlite3
import os


VISITOR_DB = "visitor.db"


def init_visitor_db():

    conn = sqlite3.connect(VISITOR_DB)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitor_stats (
            id INTEGER PRIMARY KEY,
            total_visitors INTEGER NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO visitor_stats
        (id, total_visitors)
        VALUES (1, 0)
    """)

    conn.commit()
    conn.close()


def increase_visitor_count():

    conn = sqlite3.connect(VISITOR_DB)

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE visitor_stats
        SET total_visitors = total_visitors + 1
        WHERE id = 1
    """)

    conn.commit()
    conn.close()


def get_visitor_count():

    conn = sqlite3.connect(VISITOR_DB)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT total_visitors
        FROM visitor_stats
        WHERE id = 1
    """)

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return 0
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HATCHERY_CSV = os.path.join(
    BASE_DIR,
    "data",
    "bangladesh_fish_hatcheries_current.csv"
)

FISH_CSV = os.path.join(
    BASE_DIR,
    "data",
    "fish_master.csv"
)

MAPPING_CSV = os.path.join(
    BASE_DIR,
    "data",
    "fish_hatchery_species_mapping.csv"
)

hatchery_df = pd.read_csv(HATCHERY_CSV)
fish_df = pd.read_csv(FISH_CSV)
mapping_df = pd.read_csv(MAPPING_CSV)  


# importing model
model_path = os.path.join(BASE_DIR, "model.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

#creating flask app
app = Flask(__name__)

# =========================
# Crop Details Dictionary
# =========================
crop_details = {
    "mothbeans": {
        "name_bn": "মট কলাই",
        "name_en": "Moth Beans",
        "scientific_name": "Vigna aconitifolia",
        "soil": "বেলে দোআঁশ, দোআঁশ ও সুনিষ্কাশিত হালকা মাটি",
        "temperature": "24-35°C",
        "humidity": "40-60%",
        "rainfall": "250-500 mm",
        "ph": "6.0-7.5",
        "season": "খরিফ",
        "sowing_time": "জুন-জুলাই",
        "harvest_time": "75-90 দিন",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি এবং জিপসাম",
        "irrigation": "সাধারণত বৃষ্টিনির্ভর। দীর্ঘ খরার সময় ১-২ বার হালকা সেচ দিলেই যথেষ্ট।",
        "care": "আগাছা নিয়মিত পরিষ্কার করতে হবে, সঠিক দূরত্বে বপন করতে হবে এবং জমিতে পানি জমতে দেওয়া যাবে না।",
        "weather": "উষ্ণ, শুষ্ক ও কম বৃষ্টিপাতযুক্ত জলবায়ু মট কলাই চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "ইয়েলো মোজাইক ভাইরাস, লিফ স্পট, রুট রট",
        "pests": "এফিড, থ্রিপস, পড বোরার",
        "solution": "বীজ শোধন, রোগ প্রতিরোধী জাত ব্যবহার এবং অনুমোদিত কীটনাশক ও ছত্রাকনাশক প্রয়োগ।",
        "yield": "0.8-1.5 টন/হেক্টর",
        "uses": "ডাল হিসেবে খাওয়া হয়, পশুখাদ্য হিসেবে ব্যবহৃত হয় এবং মাটির উর্বরতা বৃদ্ধির জন্য সবুজ সার হিসেবেও ব্যবহার করা হয়।",
        "image": "mothbeans.jpg"
    },
    "coffee": {
        "name_bn": "কফি",
        "name_en": "Coffee",
        "scientific_name": "Coffea arabica / Coffea canephora",
        "soil": "উর্বর দোআঁশ, বেলে দোআঁশ ও জৈব পদার্থসমৃদ্ধ সুনিষ্কাশিত মাটি",
        "temperature": "18-28°C",
        "humidity": "70-90%",
        "rainfall": "1200-2200 mm",
        "ph": "5.5-6.5",
        "season": "বর্ষাকাল চারা রোপণের জন্য উপযুক্ত",
        "sowing_time": "জুন-আগস্ট",
        "harvest_time": "রোপণের 3-4 বছর পরে ফল সংগ্রহ শুরু; নভেম্বর-ফেব্রুয়ারি ফল সংগ্রহের মৌসুম",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, ডলোমাইট, বোরন ও জিংক সালফেট",
        "irrigation": "শুষ্ক মৌসুমে ১০-১৫ দিন পরপর সেচ দিতে হবে। অতিরিক্ত পানি জমতে দেওয়া যাবে না।",
        "care": "ছায়াযুক্ত স্থানে চাষ করা ভালো। নিয়মিত আগাছা পরিষ্কার, ডাল ছাঁটাই, জৈব সার প্রয়োগ এবং রোগ-পোকার আক্রমণ পর্যবেক্ষণ করতে হবে।",
        "weather": "শীতল থেকে উষ্ণ, আর্দ্র এবং পাহাড়ি জলবায়ু কফি চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "কফি লিফ রাস্ট, বেরি ডিজিজ, রুট রট",
        "pests": "কফি বেরি বোরার, লিফ মাইনার, স্কেল ইনসেক্ট",
        "solution": "রোগ প্রতিরোধী জাত ব্যবহার, আক্রান্ত অংশ অপসারণ এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "1.5-3.0 টন/হেক্টর (শুকনো কফি বিন)",
        "uses": "কফি পানীয়, ইনস্ট্যান্ট কফি, কফি পাউডার, বেকারি পণ্য, প্রসাধনী এবং ঔষধ শিল্পে ব্যবহৃত হয়।",
        "image": "coffee.jpg"
    },
    "jute": {
        "name_bn": "পাট",
        "name_en": "Jute",
        "scientific_name": "Corchorus olitorius / Corchorus capsularis",
        "soil": "উর্বর পলি, দোআঁশ ও বেলে দোআঁশ মাটি",
        "temperature": "24-37°C",
        "humidity": "70-90%",
        "rainfall": "1500-2500 mm",
        "ph": "6.0-7.5",
        "season": "খরিফ",
        "sowing_time": "মার্চ-মে",
        "harvest_time": "120-140 দিন",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, জিপসাম এবং জিংক সালফেট",
        "irrigation": "সাধারণত বৃষ্টিনির্ভর। খরার সময় ১-২ বার সেচ প্রয়োজন হতে পারে।",
        "care": "সময়মতো আগাছা পরিষ্কার, প্রয়োজন অনুযায়ী পাতলা করা, সুষম সার প্রয়োগ এবং জমিতে পানি নিষ্কাশনের ব্যবস্থা রাখতে হবে।",
        "weather": "উষ্ণ, আর্দ্র ও পর্যাপ্ত বৃষ্টিপাতযুক্ত জলবায়ু পাট চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "স্টেম রট, অ্যানথ্রাকনোজ, লিফ ব্লাইট, উইল্ট",
        "pests": "পাটের সেমিলুপার, উইভিল, এফিড, হেয়ারি ক্যাটারপিলার",
        "solution": "রোগমুক্ত বীজ ব্যবহার, ফসল পর্যায়ক্রমে চাষ, আক্রান্ত গাছ অপসারণ এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "2.5-3.5 টন আঁশ/হেক্টর",
        "uses": "বস্তা, দড়ি, কার্পেট, জিও-টেক্সটাইল, কাগজ, হস্তশিল্প এবং পরিবেশবান্ধব প্যাকেজিং সামগ্রী তৈরিতে ব্যবহৃত হয়।",
        "image": "jute.jpg"
    },
    "cotton": {
        "name_bn": "তুলা",
        "name_en": "Cotton",
        "scientific_name": "Gossypium hirsutum",
        "soil": "উর্বর দোআঁশ, এঁটেল দোআঁশ ও সুনিষ্কাশিত কালো মাটি",
        "temperature": "21-30°C",
        "humidity": "50-70%",
        "rainfall": "600-1200 mm",
        "ph": "5.8-8.0",
        "season": "খরিফ",
        "sowing_time": "এপ্রিল-জুন",
        "harvest_time": "150-180 দিন",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, জিংক সালফেট ও বোরন",
        "irrigation": "বৃষ্টিপাত কম হলে ৩-৫ বার সেচ দিতে হবে। ফুল ও বল (Boll) গঠনের সময় পর্যাপ্ত সেচ নিশ্চিত করতে হবে।",
        "care": "নিয়মিত আগাছা পরিষ্কার, সুষম সার প্রয়োগ, গাছের সঠিক দূরত্ব বজায় রাখা এবং রোগ-পোকা নিয়মিত পর্যবেক্ষণ করতে হবে।",
        "weather": "উষ্ণ, রৌদ্রোজ্জ্বল ও মাঝারি শুষ্ক জলবায়ু তুলা চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "ব্যাকটেরিয়াল ব্লাইট, ফিউজারিয়াম উইল্ট, অল্টারনারিয়া লিফ স্পট",
        "pests": "বলওয়ার্ম, জ্যাসিড, এফিড, সাদা মাছি (Whitefly)",
        "solution": "বীজ শোধন, রোগ প্রতিরোধী জাত ব্যবহার, ফেরোমন ফাঁদ স্থাপন এবং অনুমোদিত কীটনাশক ও ছত্রাকনাশক ব্যবহার।",
        "yield": "2-4 টন/হেক্টর",
        "uses": "বস্ত্র শিল্পের কাঁচামাল, তুলার বীজ থেকে তেল উৎপাদন, পশুখাদ্য এবং বিভিন্ন শিল্পপণ্যে ব্যবহৃত হয়।",
        "image": "cotton.jpg"
    },
    "coconut": {
        "name_bn": "নারিকেল",
        "name_en": "Coconut",
        "scientific_name": "Cocos nucifera",
        "soil": "বেলে দোআঁশ, দোআঁশ ও সুনিষ্কাশিত উপকূলীয় মাটি",
        "temperature": "27-32°C",
        "humidity": "70-90%",
        "rainfall": "1500-2500 mm",
        "ph": "5.2-8.0",
        "season": "সারা বছর চাষ করা যায়, বর্ষাকালে রোপণ উত্তম",
        "sowing_time": "জুন-আগস্ট",
        "harvest_time": "রোপণের 5-7 বছর পরে ফল ধরা শুরু; পরিপক্ব ফল 11-12 মাসে সংগ্রহ করা যায়",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, ডলোমাইট, বোরন ও জিংক",
        "irrigation": "শুষ্ক মৌসুমে ১৫-২০ দিন পরপর সেচ দিতে হবে। বর্ষাকালে সাধারণত অতিরিক্ত সেচের প্রয়োজন হয় না।",
        "care": "নিয়মিত আগাছা পরিষ্কার, গাছের গোড়া পরিষ্কার রাখা, শুকনো পাতা অপসারণ এবং বছরে ২-৩ বার সুষম সার প্রয়োগ করতে হবে।",
        "weather": "উষ্ণ, আর্দ্র ও উপকূলীয় জলবায়ু নারিকেল চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "বাড রট, স্টেম ব্লিডিং, লিফ ব্লাইট",
        "pests": "রাইনোসেরোস বিটল, রেড পাম উইভিল, ব্ল্যাক-হেডেড ক্যাটারপিলার",
        "solution": "পরিষ্কার-পরিচ্ছন্ন বাগান, আক্রান্ত অংশ অপসারণ, ফেরোমন ফাঁদ ব্যবহার এবং অনুমোদিত কীটনাশক ও ছত্রাকনাশক প্রয়োগ।",
        "yield": "৮,০০০-১২,০০০টি ফল/হেক্টর/বছর (গড়ে প্রতি গাছে ৫০-১০০টি ফল)",
        "uses": "ডাব, নারিকেল, নারিকেল তেল, নারিকেলের দুধ, কোরানো নারিকেল, মিষ্টান্ন, প্রসাধনী এবং বিভিন্ন শিল্পে ব্যবহৃত হয়।",
        "image": "coconut.jpg"
    },
    "papaya": {
        "name_bn": "পেঁপে",
        "name_en": "Papaya",
        "scientific_name": "Carica papaya",
        "soil": "উর্বর বেলে দোআঁশ, দোআঁশ ও সুনিষ্কাশিত মাটি",
        "temperature": "22-33°C",
        "humidity": "60-80%",
        "rainfall": "1000-2000 mm",
        "ph": "5.5-7.0",
        "season": "সারা বছর চাষ করা যায়, তবে বর্ষা ও বসন্তে রোপণ উত্তম",
        "sowing_time": "ফেব্রুয়ারি-মার্চ অথবা জুন-জুলাই",
        "harvest_time": "রোপণের 8-10 মাস পরে ফল সংগ্রহ শুরু; 2-3 বছর পর্যন্ত ফল দেয়",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, জিপসাম, জিংক সালফেট ও বোরন",
        "irrigation": "গ্রীষ্মকালে ৭-১০ দিন পরপর এবং শীতকালে ১৫-২০ দিন পরপর সেচ দিতে হবে। পানি জমতে দেওয়া যাবে না।",
        "care": "নিয়মিত আগাছা পরিষ্কার, শুকনো পাতা অপসারণ, সুষম সার প্রয়োগ এবং রোগ-পোকার আক্রমণ পর্যবেক্ষণ করতে হবে।",
        "weather": "উষ্ণ ও আর্দ্র জলবায়ু পেঁপে চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "পেঁপে রিং স্পট ভাইরাস, অ্যানথ্রাকনোজ, পাউডারি মিলডিউ, রুট রট",
        "pests": "এফিড, মিলিবাগ, ফলমাছি, রেড স্পাইডার মাইট",
        "solution": "রোগমুক্ত চারা ব্যবহার, আক্রান্ত গাছ অপসারণ, জমিতে পানি জমতে না দেওয়া এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "40-60 টন/হেক্টর",
        "uses": "তাজা ফল, জুস, সালাদ, জ্যাম, আচার এবং প্যাপেইন এনজাইম উৎপাদনে ব্যবহৃত হয়।",
        "image": "papaya.jpg"
    },
    "orange": {
        "name_bn": "কমলা",
        "name_en": "Orange",
        "scientific_name": "Citrus sinensis",
        "soil": "উর্বর বেলে দোআঁশ, দোআঁশ ও সুনিষ্কাশিত মাটি",
        "temperature": "18-30°C",
        "humidity": "50-70%",
        "rainfall": "1000-1500 mm",
        "ph": "5.5-6.5",
        "season": "বসন্ত ও বর্ষাকাল",
        "sowing_time": "জুন-আগস্ট অথবা ফেব্রুয়ারি-মার্চ",
        "harvest_time": "রোপণের 3-4 বছর পরে; ফল সংগ্রহ নভেম্বর-ফেব্রুয়ারি",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, জিংক সালফেট ও বোরন",
        "irrigation": "শুষ্ক মৌসুমে ১০-১৫ দিন পরপর সেচ দিতে হবে। অতিরিক্ত পানি জমতে দেওয়া যাবে না।",
        "care": "নিয়মিত আগাছা পরিষ্কার, গাছ ছাঁটাই, শুকনো ও রোগাক্রান্ত ডাল অপসারণ এবং সুষম সার প্রয়োগ করতে হবে।",
        "weather": "উষ্ণ ও আর্দ্র উপ-ক্রান্তীয় জলবায়ু কমলা চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "সাইট্রাস ক্যানকার, গামোসিস, অ্যানথ্রাকনোজ",
        "pests": "সাইট্রাস লিফ মাইনার, এফিড, ফলমাছি, স্কেল পোকা",
        "solution": "রোগমুক্ত চারা ব্যবহার, আক্রান্ত ডাল অপসারণ এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ।",
        "yield": "15-30 টন/হেক্টর",
        "uses": "তাজা ফল, জুস, জ্যাম, মার্মালেড, মিষ্টান্ন এবং ভিটামিন-সি সমৃদ্ধ খাদ্য হিসেবে ব্যবহৃত হয়।",
        "image": "orange.jpg"
    },
    "apple": {
        "name_bn": "আপেল",
        "name_en": "Apple",
        "scientific_name": "Malus domestica",
        "soil": "উর্বর দোআঁশ, বেলে দোআঁশ ও সুনিষ্কাশিত মাটি",
        "temperature": "18-24°C",
        "humidity": "60-75%",
        "rainfall": "800-1200 mm",
        "ph": "5.5-6.8",
        "season": "শীতপ্রধান অঞ্চলে চাষের উপযোগী",
        "sowing_time": "ডিসেম্বর-ফেব্রুয়ারি (চারা রোপণ)",
        "harvest_time": "রোপণের 3-5 বছর পরে; ফল সংগ্রহ আগস্ট-অক্টোবর",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, ক্যালসিয়াম ও বোরন",
        "irrigation": "শুষ্ক মৌসুমে ১০-১৫ দিন পরপর সেচ দিতে হবে। অতিরিক্ত পানি জমতে দেওয়া যাবে না।",
        "care": "নিয়মিত গাছ ছাঁটাই, আগাছা পরিষ্কার, সুষম সার প্রয়োগ এবং রোগ-পোকা নিয়মিত পর্যবেক্ষণ করতে হবে।",
        "weather": "শীতল ও নাতিশীতোষ্ণ জলবায়ু আপেল চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "অ্যাপল স্ক্যাব, পাউডারি মিলডিউ, ফায়ার ব্লাইট",
        "pests": "কডলিং মথ, এফিড, স্পাইডার মাইট",
        "solution": "রোগমুক্ত চারা ব্যবহার, আক্রান্ত অংশ অপসারণ এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ।",
        "yield": "20-40 টন/হেক্টর",
        "uses": "তাজা ফল, জুস, জ্যাম, জেলি, পাই, শুকনো ফল এবং বিভিন্ন খাদ্যপণ্য তৈরিতে ব্যবহৃত হয়।",
        "image": "apple.jpg"
    },
    "muskmelon": {
        "name_bn": "বাঙ্গি",
        "name_en": "Muskmelon",
        "scientific_name": "Cucumis melo",
        "soil": "বেলে দোআঁশ, দোআঁশ ও সুনিষ্কাশিত উর্বর মাটি",
        "temperature": "24-35°C",
        "humidity": "60-70%",
        "rainfall": "400-700 mm",
        "ph": "6.0-7.5",
        "season": "রবি ও গ্রীষ্মকাল",
        "sowing_time": "জানুয়ারি-মার্চ",
        "harvest_time": "75-90 দিন",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, জিপসাম এবং বোরন",
        "irrigation": "৭-১০ দিন পরপর হালকা সেচ দিতে হবে। ফল পাকতে শুরু করলে সেচ কমিয়ে দিতে হবে।",
        "care": "নিয়মিত আগাছা পরিষ্কার, লতা ছড়িয়ে দেওয়া, সুষম সার প্রয়োগ এবং ফল মাটির সংস্পর্শে না রাখার ব্যবস্থা করতে হবে।",
        "weather": "উষ্ণ, রৌদ্রোজ্জ্বল ও শুষ্ক আবহাওয়া বাঙ্গি চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "পাউডারি মিলডিউ, ডাউনি মিলডিউ, ফিউজারিয়াম উইল্ট, অ্যানথ্রাকনোজ",
        "pests": "ফলমাছি, এফিড, লাল মাকড়, থ্রিপস",
        "solution": "রোগমুক্ত বীজ ব্যবহার, জমিতে পানি জমতে না দেওয়া এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "20-30 টন/হেক্টর",
        "uses": "তাজা ফল, জুস, ফলের সালাদ, ডেজার্ট এবং পুষ্টিকর খাদ্য হিসেবে ব্যবহৃত হয়।",
        "image": "muskmelon.jpg"
    },
    "watermelon": {
        "name_bn": "তরমুজ",
        "name_en": "Watermelon",
        "scientific_name": "Citrullus lanatus",
        "soil": "বেলে দোআঁশ, দোআঁশ ও সুনিষ্কাশিত উর্বর মাটি",
        "temperature": "22-35°C",
        "humidity": "60-70%",
        "rainfall": "500-800 mm",
        "ph": "6.0-7.5",
        "season": "রবি ও গ্রীষ্মকাল",
        "sowing_time": "ডিসেম্বর-ফেব্রুয়ারি",
        "harvest_time": "80-100 দিন",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, জিপসাম ও বোরন",
        "irrigation": "৭-১০ দিন পরপর সেচ দিতে হবে। ফল পরিপক্ব হওয়ার আগে অতিরিক্ত সেচ এড়িয়ে চলতে হবে।",
        "care": "আগাছা পরিষ্কার, লতা সঠিকভাবে ছড়িয়ে দেওয়া, ফল মাটির সংস্পর্শ থেকে রক্ষা করা এবং সুষম সার প্রয়োগ করতে হবে।",
        "weather": "উষ্ণ, রৌদ্রোজ্জ্বল ও শুষ্ক আবহাওয়া সবচেয়ে উপযোগী।",
        "disease": "পাউডারি মিলডিউ, ডাউনি মিলডিউ, ফিউজারিয়াম উইল্ট, অ্যানথ্রাকনোজ",
        "pests": "ফলমাছি, এফিড, লাল মাকড়, থ্রিপস",
        "solution": "ফসল পর্যায়ক্রমে চাষ, রোগমুক্ত বীজ ব্যবহার এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ।",
        "yield": "25-40 টন/হেক্টর",
        "uses": "তাজা ফল, জুস, ফলের সালাদ, স্মুদি এবং বীজ ভেজে খাওয়ার জন্য ব্যবহৃত হয়।",
        "image": "watermelon.jpg"
    },
    "grapes": {
        "name_bn": "আঙুর",
        "name_en": "Grapes",
        "scientific_name": "Vitis vinifera",
        "soil": "বেলে দোআঁশ, দোআঁশ ও সুনিষ্কাশিত উর্বর মাটি",
        "temperature": "15-35°C",
        "humidity": "50-70%",
        "rainfall": "500-900 mm",
        "ph": "6.0-7.5",
        "season": "শীতের শেষে বা বসন্তে রোপণ উপযোগী",
        "sowing_time": "জানুয়ারি-মার্চ",
        "harvest_time": "রোপণের 2-3 বছর পরে; ফল সংগ্রহ মে-জুলাই",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি এবং মাইক্রোনিউট্রিয়েন্ট",
        "irrigation": "গ্রীষ্মকালে ৭-১০ দিন পরপর সেচ এবং বর্ষাকালে প্রয়োজন অনুযায়ী সেচ দিতে হবে।",
        "care": "লতা নিয়মিত ছাঁটাই, মাচা তৈরি, আগাছা পরিষ্কার এবং সুষম সার প্রয়োগ করতে হবে।",
        "weather": "উষ্ণ ও শুষ্ক জলবায়ু আঙুর চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "পাউডারি মিলডিউ, ডাউনি মিলডিউ, অ্যানথ্রাকনোজ",
        "pests": "মিলিবাগ, থ্রিপস, ফলমাছি",
        "solution": "নিয়মিত ছাঁটাই, আক্রান্ত অংশ অপসারণ এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "15-25 টন/হেক্টর",
        "uses": "তাজা ফল, কিশমিশ, জুস, জ্যাম, জেলি এবং বিভিন্ন খাদ্যপণ্য তৈরিতে ব্যবহৃত হয়।",
        "image": "grapes.jpg"
    },
    "mango": {
        "name_bn": "আম",
        "name_en": "Mango",
        "scientific_name": "Mangifera indica",
        "soil": "উর্বর দোআঁশ, বেলে দোআঁশ ও সুনিষ্কাশিত পলি মাটি",
        "temperature": "24-30°C",
        "humidity": "50-70%",
        "rainfall": "750-2500 mm",
        "ph": "5.5-7.5",
        "season": "বসন্তে ফুল আসে, গ্রীষ্মে ফল সংগ্রহ",
        "sowing_time": "জুন-আগস্ট (চারা রোপণের উপযুক্ত সময়)",
        "harvest_time": "রোপণের 3-5 বছর পরে ফল আসা শুরু; মে-জুলাই মাসে ফল সংগ্রহ",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, জিপসাম ও জিংক সালফেট",
        "irrigation": "শুষ্ক মৌসুমে ১৫-২০ দিন পরপর সেচ দিতে হবে। বর্ষাকালে সাধারণত অতিরিক্ত সেচের প্রয়োজন হয় না।",
        "care": "নিয়মিত আগাছা পরিষ্কার, গাছ ছাঁটাই, শুকনো ও রোগাক্রান্ত ডাল অপসারণ এবং সুষম সার প্রয়োগ করতে হবে।",
        "weather": "উষ্ণ ও অপেক্ষাকৃত শুষ্ক জলবায়ু আম চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "অ্যানথ্রাকনোজ, পাউডারি মিলডিউ, ডাই-ব্যাক",
        "pests": "ম্যাঙ্গো হপার, ফলমাছি, মিলিবাগ",
        "solution": "বাগান পরিষ্কার রাখা, আক্রান্ত অংশ অপসারণ এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "10-20 টন/হেক্টর",
        "uses": "তাজা ফল, জুস, আচার, জ্যাম, আমচুর, শুকনো আম এবং বিভিন্ন খাদ্যপণ্য তৈরিতে ব্যবহৃত হয়।",
        "image": "mango.jpg"
    },
    "banana": {
        "name_bn": "কলা",
        "name_en": "Banana",
        "scientific_name": "Musa spp.",
        "soil": "উর্বর দোআঁশ, বেলে দোআঁশ ও সুনিষ্কাশিত পলি মাটি",
        "temperature": "26-30°C",
        "humidity": "75-85%",
        "rainfall": "1000-2500 mm",
        "ph": "5.5-7.0",
        "season": "সারা বছর (বর্ষাকাল রোপণের জন্য সবচেয়ে উপযোগী)",
        "sowing_time": "ফেব্রুয়ারি-এপ্রিল অথবা জুলাই-সেপ্টেম্বর",
        "harvest_time": "রোপণের 10-15 মাস পরে",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি, জিপসাম ও জিংক সালফেট",
        "irrigation": "গ্রীষ্মে প্রতি ৭-১০ দিন পরপর এবং শীতকালে ১৫-২০ দিন পরপর সেচ দিতে হবে।",
        "care": "নিয়মিত আগাছা পরিষ্কার, শুকনো পাতা অপসারণ, গাছে খুঁটি দেওয়া এবং সময়মতো সার প্রয়োগ করতে হবে।",
        "weather": "উষ্ণ ও আর্দ্র জলবায়ু কলা চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "পানামা উইল্ট, সিগাটোকা লিফ স্পট, বান্চি টপ ভাইরাস",
        "pests": "কলার উইভিল, এফিড, নিমাটোড",
        "solution": "রোগমুক্ত চারা ব্যবহার, আক্রান্ত গাছ অপসারণ এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ।",
        "yield": "30-60 টন/হেক্টর",
        "uses": "তাজা ফল, চিপস, জুস, মিষ্টান্ন, শিশু খাদ্য এবং বিভিন্ন খাদ্যপণ্য তৈরিতে ব্যবহৃত হয়।",
        "image": "banana.jpg"
    },  
    "pomegranate": {
        "name_bn": "ডালিম",
        "name_en": "Pomegranate",
        "scientific_name": "Punica granatum",
        "soil": "বেলে দোআঁশ, দোআঁশ ও সুনিষ্কাশিত মাটি",
        "temperature": "20-35°C",
        "humidity": "40-60%",
        "rainfall": "500-1000 mm",
        "ph": "5.5-7.5",
        "season": "বসন্ত ও বর্ষাকাল রোপণের জন্য উপযুক্ত",
        "sowing_time": "ফেব্রুয়ারি-মার্চ অথবা জুলাই-আগস্ট",
        "harvest_time": "রোপণের ১৮০-২১০ দিন পরে ফল সংগ্রহ শুরু; পূর্ণ ফলন ২-৩ বছরে",
        "fertilizer": "জৈব সার, ইউরিয়া, টিএসপি, এমওপি এবং জিংক সালফেট",
        "irrigation": "গ্রীষ্মকালে ৭-১০ দিন পরপর সেচ এবং শীতকালে ১৫-২০ দিন পরপর সেচ দিতে হবে।",
        "care": "নিয়মিত ছাঁটাই, আগাছা পরিষ্কার, রোগাক্রান্ত ডাল অপসারণ এবং সুষম সার প্রয়োগ করতে হবে।",
        "weather": "উষ্ণ ও শুষ্ক জলবায়ু সবচেয়ে উপযোগী।",
        "disease": "ব্যাকটেরিয়াল ব্লাইট, ফল পচা, লিফ স্পট",
        "pests": "ফল ছিদ্রকারী পোকা, এফিড, মিলিবাগ",
        "solution": "পরিষ্কার-পরিচ্ছন্ন বাগান, আক্রান্ত অংশ অপসারণ এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "১০-২০ টন/হেক্টর",
        "uses": "তাজা ফল, জুস, জ্যাম, ঔষধি ব্যবহার এবং অ্যান্টিঅক্সিডেন্ট সমৃদ্ধ স্বাস্থ্যকর খাদ্য।",
        "image": "pomegranate.jpg"
    },
    "lentil": {
        "name_bn": "মসুর ডাল",
        "name_en": "Lentil",
        "scientific_name": "Lens culinaris",
        "soil": "উর্বর দোআঁশ, বেলে দোআঁশ ও সুনিষ্কাশিত পলি মাটি",
        "temperature": "18-25°C",
        "humidity": "40-60%",
        "rainfall": "300-500 mm",
        "ph": "6.0-7.5",
        "season": "রবি",
        "sowing_time": "অক্টোবর-নভেম্বর",
        "harvest_time": "100-120 দিন",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি, জিপসাম এবং জৈব সার",
        "irrigation": "সাধারণত ১-২ বার হালকা সেচ যথেষ্ট। জমিতে পানি জমতে দেওয়া যাবে না।",
        "care": "উন্নত জাতের বীজ ব্যবহার, আগাছা নিয়ন্ত্রণ, সময়মতো সার প্রয়োগ এবং রোগ-পোকার আক্রমণ নিয়মিত পর্যবেক্ষণ করতে হবে।",
        "weather": "শীতল ও শুষ্ক আবহাওয়া মসুর চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "রস্ট, উইল্ট, রুট রট, অ্যাসকোকাইটা ব্লাইট",
        "pests": "এফিড, কাটওয়ার্ম, পড বোরার",
        "solution": "বীজ শোধন, রোগ প্রতিরোধী জাত নির্বাচন এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "১.২-২.০ টন/হেক্টর",
        "uses": "ডাল, স্যুপ, খিচুড়ি, বিভিন্ন রান্না এবং উচ্চ প্রোটিনসমৃদ্ধ খাদ্য হিসেবে ব্যবহৃত হয়।",
        "image": "lentil.jpg"
    },
    "blackgram": {
        "name_bn": "মাষকলাই",
        "name_en": "Black Gram",
        "scientific_name": "Vigna mungo",
        "soil": "উর্বর দোআঁশ, বেলে দোআঁশ ও সুনিষ্কাশিত পলি মাটি",
        "temperature": "25-35°C",
        "humidity": "50-70%",
        "rainfall": "600-1000 mm",
        "ph": "6.0-7.5",
        "season": "খরিফ ও রবি",
        "sowing_time": "ফেব্রুয়ারি-মার্চ এবং জুলাই-আগস্ট",
        "harvest_time": "70-90 দিন",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি, জিপসাম এবং জৈব সার",
        "irrigation": "সাধারণত ১-২ বার সেচ যথেষ্ট। অতিরিক্ত পানি জমতে দেওয়া যাবে না।",
        "care": "উন্নত মানের বীজ ব্যবহার, নিয়মিত আগাছা পরিষ্কার, সময়মতো সার প্রয়োগ এবং রোগ-পোকার আক্রমণ পর্যবেক্ষণ করতে হবে।",
        "weather": "উষ্ণ ও মাঝারি আর্দ্র জলবায়ু মাষকলাই চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "ইয়েলো মোজাইক ভাইরাস, লিফ স্পট, পাউডারি মিলডিউ",
        "pests": "এফিড, থ্রিপস, পড বোরার",
        "solution": "বীজ শোধন, রোগ প্রতিরোধী জাত নির্বাচন এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার।",
        "yield": "১.০-১.৮ টন/হেক্টর",
        "uses": "ডাল, বড়া, পাপড়, বিভিন্ন খাদ্যপণ্য এবং উচ্চ প্রোটিনসমৃদ্ধ খাবার তৈরিতে ব্যবহৃত হয়।",
        "image": "blackgram.jpg"
    },
    "mungbean": {
        "name_bn": "মুগ ডাল",
        "name_en": "Mung Bean",
        "scientific_name": "Vigna radiata",
        "soil": "দোআঁশ, বেলে দোআঁশ ও সুনিষ্কাশিত পলি মাটি",
        "temperature": "25-35°C",
        "humidity": "50-70%",
        "rainfall": "600-900 mm",
        "ph": "6.0-7.5",
        "season": "খরিফ ও রবি",
        "sowing_time": "ফেব্রুয়ারি-মার্চ এবং জুলাই-আগস্ট",
        "harvest_time": "60-75 দিন",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি, জিপসাম এবং জৈব সার",
        "irrigation": "প্রয়োজনে ১-২ বার হালকা সেচ দিতে হবে। জমিতে পানি জমতে দেওয়া যাবে না।",
        "care": "উন্নত বীজ ব্যবহার, নিয়মিত আগাছা পরিষ্কার, সঠিক সময়ে সার প্রয়োগ এবং রোগ-পোকার আক্রমণ পর্যবেক্ষণ করতে হবে।",
        "weather": "উষ্ণ ও মাঝারি আর্দ্র জলবায়ু মুগ ডাল চাষের জন্য সবচেয়ে উপযোগী।",
        "disease": "পাউডারি মিলডিউ, ইয়েলো মোজাইক ভাইরাস, লিফ স্পট",
        "pests": "এফিড, থ্রিপস, পড বোরার",
        "solution": "বীজ শোধন, রোগ প্রতিরোধী জাত ব্যবহার এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ।",
        "yield": "১.০-১.৮ টন/হেক্টর",
        "uses": "ডাল, অঙ্কুরিত শস্য (Sprouts), বিভিন্ন মিষ্টান্ন, স্যুপ এবং উচ্চ প্রোটিনসমৃদ্ধ খাদ্য হিসেবে ব্যবহৃত হয়।",
        "image": "mungbean.jpg"
    },
    "pigeonpeas": {
        "name_bn": "অড়হর ডাল",
        "name_en": "Pigeon Peas",
        "scientific_name": "Cajanus cajan",
        "soil": "দোআঁশ, বেলে দোআঁশ ও সুনিষ্কাশিত পলি মাটি",
        "temperature": "20-35°C",
        "humidity": "50-70%",
        "rainfall": "600-1000 mm",
        "ph": "5.5-7.5",
        "season": "খরিফ",
        "sowing_time": "জুন-জুলাই",
        "harvest_time": "150-180 দিন",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি, জিপসাম এবং জৈব সার",
        "irrigation": "সাধারণত বৃষ্টির পানিই যথেষ্ট। খরার সময় ১-২ বার সেচ দিলে ভালো ফলন পাওয়া যায়।",
        "care": "উন্নত জাতের বীজ ব্যবহার, আগাছা নিয়ন্ত্রণ, পানি নিষ্কাশনের ব্যবস্থা রাখা এবং সময়মতো সার প্রয়োগ করতে হবে।",
        "weather": "উষ্ণ ও মাঝারি আর্দ্র জলবায়ু সবচেয়ে উপযোগী।",
        "disease": "উইল্ট, ফিউজারিয়াম ব্লাইট, স্টেরিলিটি মোজাইক",
        "pests": "পড বোরার, এফিড, লিফ হপার",
        "solution": "বীজ শোধন, রোগ প্রতিরোধী জাত ব্যবহার এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ।",
        "yield": "১.৫-২.৫ টন/হেক্টর",
        "uses": "ডাল হিসেবে রান্না, পশুখাদ্য এবং মাটির উর্বরতা বৃদ্ধিতে সবুজ সার হিসেবে ব্যবহৃত হয়।",
        "image": "pigeonpeas.jpg"
    },
    "kidneybeans": {
        "name_bn": "রাজমা",
        "name_en": "Kidney Beans",
        "scientific_name": "Phaseolus vulgaris",
        "soil": "উর্বর দোআঁশ ও বেলে দোআঁশ মাটি",
        "temperature": "18-27°C",
        "humidity": "50-65%",
        "rainfall": "400-700 mm",
        "ph": "6.0-7.5",
        "season": "রবি",
        "sowing_time": "অক্টোবর-নভেম্বর",
        "harvest_time": "90-120 দিন",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি এবং জৈব সার",
        "irrigation": "২-৩ বার হালকা সেচ প্রয়োজন। জমিতে পানি জমতে দেওয়া যাবে না।",
        "care": "উন্নত জাতের বীজ ব্যবহার, নিয়মিত আগাছা পরিষ্কার, সঠিক সময়ে সার প্রয়োগ এবং রোগ-পোকা পর্যবেক্ষণ করতে হবে।",
        "weather": "শীতল ও মাঝারি শুষ্ক আবহাওয়া চাষের জন্য উপযুক্ত।",
        "disease": "অ্যানথ্রাকনোজ, রুট রট, পাউডারি মিলডিউ",
        "pests": "এফিড, বিন বিটল, পড বোরার",
        "solution": "বীজ শোধন, রোগ প্রতিরোধী জাত ব্যবহার এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ।",
        "yield": "২-৩ টন/হেক্টর",
        "uses": "উচ্চ প্রোটিনসমৃদ্ধ খাদ্য, স্যুপ, সালাদ, তরকারি এবং বিভিন্ন প্রক্রিয়াজাত খাদ্য তৈরিতে ব্যবহৃত হয়।",
        "image": "kidneybeans.jpg"
    },
    "chickpea": {
        "name_bn": "ছোলা",
        "name_en": "Chickpea",
        "scientific_name": "Cicer arietinum",
        "soil": "দোআঁশ, বেলে দোআঁশ ও সুনিষ্কাশিত মাটি",
        "temperature": "20-30°C",
        "humidity": "40-60%",
        "rainfall": "400-600 mm",
        "ph": "6.0-7.5",
        "season": "রবি",
        "sowing_time": "অক্টোবর-নভেম্বর",
        "harvest_time": "90-120 দিন",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি এবং জিপসাম",
        "irrigation": "সাধারণত ১-২ বার সেচ যথেষ্ট। অতিরিক্ত পানি ক্ষতিকর।",
        "care": "উন্নত বীজ ব্যবহার, আগাছা পরিষ্কার, পানি জমতে না দেওয়া এবং সময়মতো সার প্রয়োগ।",
        "weather": "শীতল ও শুষ্ক জলবায়ু সবচেয়ে উপযোগী।",
        "disease": "উইল্ট, অ্যাসকোকাইটা ব্লাইট, রুট রট",
        "pests": "পড বোরার, এফিড",
        "solution": "রোগমুক্ত বীজ ব্যবহার, বীজ শোধন এবং অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ।",
        "yield": "১.৫-২.৫ টন/হেক্টর",
        "uses": "ডাল, ভাজা ছোলা, বেসন, বিভিন্ন খাদ্যপণ্য এবং উচ্চ প্রোটিনসমৃদ্ধ খাদ্য হিসেবে ব্যবহৃত হয়।",
        "image": "chickpea.jpg"
    },
    "maize": {
        "name_bn": "ভুট্টা",
        "name_en": "Maize",
        "scientific_name": "Zea mays",
        "soil": "উর্বর দোআঁশ, বেলে দোআঁশ ও পলি মাটি",
        "temperature": "20-30°C",
        "humidity": "50-70%",
        "rainfall": "500-800 mm",
        "ph": "5.8-7.0",
        "season": "রবি ও খরিফ",
        "sowing_time": "অক্টোবর-নভেম্বর (রবি), ফেব্রুয়ারি-মার্চ (খরিফ)",
        "harvest_time": "90-120 দিন",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি, জিংক সালফেট ও বোরন",
        "irrigation": "৩-৪ বার সেচ প্রয়োজন, বিশেষ করে ফুল ও দানা গঠনের সময়।",
        "care": "উন্নত বীজ ব্যবহার, আগাছা পরিষ্কার, সঠিক সময়ে সার প্রয়োগ এবং জমিতে পানি জমতে না দেওয়া।",
        "weather": "উষ্ণ ও মাঝারি আর্দ্র জলবায়ু সবচেয়ে উপযোগী।",
        "disease": "লিফ ব্লাইট, ডাউনি মিলডিউ, স্টেম রট",
        "pests": "ফল আর্মিওয়ার্ম, স্টেম বোরার, কাটওয়ার্ম",
        "solution": "রোগমুক্ত বীজ ব্যবহার, অনুমোদিত ছত্রাকনাশক ও কীটনাশক প্রয়োগ এবং নিয়মিত জমি পর্যবেক্ষণ।",
        "yield": "৮-১২ টন/হেক্টর",
        "uses": "খাদ্য, পশুখাদ্য, পোল্ট্রি ফিড, কর্ন ফ্লাওয়ার, কর্ন অয়েল এবং শিল্পকারখানার কাঁচামাল।",
        "image": "maize.jpg"
    },
    "rice": {
        "bangla_name": "ধান",
        "english_name": "Rice",
        "scientific_name": "Oryza sativa",
        "season": "খরিফ (আউশ, আমন) ও রবি (বোরো)",
        "soil": "দোআঁশ অথবা এটেল মাটি",
        "temperature": "20°C - 35°C",
        "humidity": "70% - 90%",
        "rainfall": "1000-2000 mm",
        "ph": "5.5 - 6.5",
        "Aus": "March - April",
        "Aman": "June - July",
        "Boro": "November - December",
        "Aus": "July - August",
        "Aman": "November - December",
        "Boro": "April - May",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি",
        "irrigation": "নিয়মিত সেচ দিতে হবে এবং জমিতে পর্যাপ্ত পানি ধরে রাখতে হবে।",
        "care": "সঠিক সময়ে সেচ দিতে হবে। আগাছা পরিষ্কার রাখতে হবে।",
        "disease": "ব্লাস্ট রোগ,শীথ ব্লাইট,ব্রাউন স্পট",
        "pests":"মাজরা পোকা ,বাদামী গাছফড়িং ,পাতামোড়ানো পোকা",
        "solution": "অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার করুন এবং জমি পরিষ্কার রাখুন।",
        "expected_yield" : "4-7 ton/hectare",
        "uses": "ভাত,চাল,চিড়া,মুড়ি ,চালের গুঁড়া ,পশুখাদ্য",
        "image":"rice.jpg"
    },
    "wheat": {
        "English_name": "Wheat",
        "bangla_name": "গম",
        "scientific_name": "Triticum aestivum",
        "soil": "দোআঁশ মাটি",
        "weather": "15-25°C",
        "humidity": "50-70%",
        "rainfall": "300-500 মিমি",
        "ph": "6.0-7.5",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি",
        "irrigation": "২-৩ বার সেচ প্রয়োজন",
        "care": "আগাছা পরিষ্কার রাখতে হবে এবং সময়মতো সেচ দিতে হবে",
        "disease": "পাতার মরিচা, ব্লাস্ট",
        "pests": "এফিড, আর্মিওয়ার্ম",
        "solution": "অনুমোদিত ছত্রাকনাশক ও কীটনাশক ব্যবহার করুন",
        "harvest": "100-120 দিন",
        "yield": "3-5 টন/হেক্টর",
        "uses": "আটা, ময়দা, সুজি, রুটি, বিস্কুট",
        "image": "wheat.jpg"
    },
    "maize": {
        "name": "Maize",
        "bangla_name": "ভুট্টা",
        "scientific_name": "Zea mays",
        "soil": "দোআঁশ মাটি",
        "weather": "20-30°C",
        "humidity": "60-80%",
        "rainfall": "500-800 মিমি",
        "ph": "5.8-7.0",
        "fertilizer": "ইউরিয়া, টিএসপি, এমওপি",
        "irrigation": "৩-৪ বার সেচ প্রয়োজন",
        "care": "নিয়মিত সেচ দিতে হবে এবং আগাছা পরিষ্কার রাখতে হবে",
        "disease": "পাতা ঝলসানো রোগ, মরিচা রোগ",
        "pests": "ফল আর্মিওয়ার্ম, স্টেম বোরার",
        "solution": "অনুমোদিত কীটনাশক ও ছত্রাকনাশক ব্যবহার করুন",
        "harvest": "90-120 দিন",
        "yield": "6-10 টন/হেক্টর",
        "uses": "খাদ্য, পশুখাদ্য, স্টার্চ ও ভোজ্য তেল উৎপাদনে ব্যবহৃত",
        "image": "maize.jpg"
    },
}
    
init_visitor_db()
@app.route("/")
def home():

    increase_visitor_count()

    return render_template("home.html")

@app.route("/crop-recommendation")
def index():
    return render_template(
"index.html",
crop=None,
details=None,
prediction=None,
confidence=None
)
@app.route("/live-stock")
def live_stock():
    return render_template("live_stock.html")
@app.route("/aquaculture")
def aquaculture():
    return render_template("aquaculture.html")
# BIOFLOC
@app.route("/biofloc")
def biofloc():
    return render_template("biofloc.html")
@app.route("/ras")
def ras():
    return render_template("ras.html")
@app.route("/cage-culture")
def cage_culture():
    return render_template("cage_culture.html")
@app.route("/marine-culture")
def marine_culture():
    return render_template("marine_culture.html")

@app.route("/weather-info")
def weather_info():
    return render_template("weather.html")
@app.route("/agriculture-office")
def agriculture_office():
    return render_template("agriculture_office.html")
@app.route('/market-price')
def market_price():
    return render_template('market_price.html')
@app.route('/fish-information')
def fish_information():
    return render_template('fish_information.html')
@app.route("/more")
def more():
    return render_template("more.html")
@app.route("/about-app")
def about_app():
    return render_template("about_app.html")
@app.route("/developers")
def developers():
    return render_template("developers.html")
@app.route("/user-guide")
def user_guide():
    return render_template("user_guide.html")
@app.route("/visitor-statistics")
def visitor_statistics():

    visitor_count = get_visitor_count()

    return render_template(
        "visitor_statistics.html",
        visitor_count=visitor_count
    )

@app.route("/fish-hatchery")
def fish_hatchery():

    hatcheries = hatchery_df.fillna("").to_dict(
        orient="records"
    )

    fishes = fish_df.fillna("").to_dict(
        orient="records"
    )

    mappings = mapping_df.fillna("").to_dict(
        orient="records"
    )

    return render_template(
        "fish_hatchery.html",
        hatcheries=hatcheries,
        fishes=fishes,
        mappings=mappings
    )





# ==============================
# POND CULTURE
# ==============================

@app.route("/pond-prediction", methods=["GET", "POST"])
def pond_prediction():

    if request.method == "POST":

        try:

            pond_size = float(request.form["pond_size"])
            pond_depth = float(request.form["pond_depth"])
            temperature = float(request.form["temperature"])
            ph = float(request.form["ph"])
            do = float(request.form["do"])
            turbidity = float(request.form["turbidity"])

        except ValueError:

            return render_template(
                "pond_prediction.html",
                error="Please enter valid numeric values."
            )


        # ==========================================
        # ML PREDICTION
        # ==========================================

        try:

            result = predict_fish(
                pond_size=pond_size,
                pond_depth=pond_depth,
                temperature=temperature,
                ph=ph,
                do=do,
                turbidity=turbidity
            )

        except Exception as error:

            return render_template(
                "pond_prediction.html",
                error=f"Prediction error: {error}"
            )


        # SHOW RESULT

        return render_template(
            "pond_prediction.html",
            result=result
        )


    return render_template(
        "pond_prediction.html"
    )
@app.route("/api/biofloc/predict", methods=["POST"])
def biofloc_predict():

    data = request.get_json()

    result = calculate_biofloc(
        fish_name=data["fish_name"],
        tank_volume_liter=float(data["tank_volume_liter"]),
        fish_count=int(data["fish_count"]),
        average_weight_g=float(data["average_weight_g"]),
        temperature=float(data["temperature"]),
        ph=float(data["ph"]),
        dissolved_oxygen=float(data["dissolved_oxygen"]),
        ammonia=float(data["ammonia"]),
        nitrite=float(data["nitrite"]),
        alkalinity=float(data["alkalinity"]),
        feed_protein=float(data["feed_protein"])
    )

    return jsonify({
        "success": True,
        "result": result
    })




@app.route("/predict", methods=["POST"])
def predict():
    N = int(request.form["Nitrogen"])
    P = int(request.form["Phosphorus"])
    K = int(request.form["Potassium"])
    Temp = float(request.form["Temperature"])
    Humidity = float(request.form["Humidity"])
    pH = float(request.form["pH"])
    Rainfall = float(request.form["Rainfall"])

    single_pred = scaler.transform(
        [[N, P, K, Temp, Humidity, pH, Rainfall]]
    )

    prediction = model.predict(single_pred)[0]

    confidence = max(model.predict_proba(single_pred)[0])


    if N < 0 or N > 140:
        return render_template(
            "index.html",
            result="❌ Nitrogen must be between 0 and 140"
        )

    if P < 0 or P > 145:
        return render_template(
            "index.html",
            result="❌ Phosphorus must be between 0 and 145"
        )

    if K < 0 or K > 205:
        return render_template(
            "index.html",
            result="❌ Potassium must be between 0 and 205"
        )

    if Temp < -10 or Temp > 60:
        return render_template(
            "index.html",
            result="❌ Temperature must be between -10°C and 60°C"
        )

    if Humidity < 0 or Humidity > 100:
        return render_template(
            "index.html",
            result="❌ Humidity must be between 0 and 100"
        )

    if pH < 0 or pH > 14:
        return render_template(
            "index.html",
            result="❌ pH must be between 0 and 14"
        )

    if Rainfall < 0:
        return render_template(
            "index.html",
            result="❌ Rainfall cannot be negative"
        )


    feature_list = [
        N, P, K, Temp, Humidity, pH, Rainfall
    ]

    single_pred = np.array(feature_list).reshape(1, -1)

    probabilities = model.predict_proba(single_pred)[0]
    
    


    # ==========================
    # Crop Dictionary

    crop_dict = {
        1: "rice",
        2: "maize",
        3: "jute",
        4: "cotton",
        5: "coconut",
        6: "papaya",
        7: "orange",
        8: "apple",
        9: "muskmelon",
        10: "watermelon",
        11: "grapes",
        12: "mango",
        13: "banana",
        14: "pomegranate",
        15: "lentil",
        16: "blackgram",
        17: "mungbean",
        18: "mothbeans",
        19: "pigeonpeas",
        20: "kidneybeans",
        21: "coffee",
        22: "chickpea"
    }


    # ==========================
    # Top 3 Recommended Crops
    # ==========================

    top_indices = np.argsort(probabilities)[::-1][:4]

    top3 = []

    for i in top_indices:

        crop_name = crop_dict[i + 1]

        # Main prediction বাদ দেওয়া
        if crop_name != prediction:

            top3.append({
                "name": crop_name,
                "image": crop_name + ".jpg",
                "confidence": round(
                    probabilities[i] * 100,
                    2
                )
            })

    top3 = top3[:3]


    # ==========================
    # Confidence
    # ==========================

    confidence = np.max(probabilities) * 100

    if confidence >= 95:
        level = "Excellent"

    elif confidence >= 80:
        level = "Good"

    else:
        level = "Low"


    print(feature_list)
    print(type(model))


    # ==========================
    # Final Prediction
    # ==========================

    prediction = model.predict(single_pred)[0]

    confidence = (
        max(model.predict_proba(single_pred)[0]) * 100
    )

    crop = crop_dict[prediction]


    # ==========================
    # Crop Details
    # ==========================

    details = crop_details.get(crop)

    image = (
        details["image"]
        if details
        else "default.jpg"
    )


    return render_template(
        "index.html",

        prediction=crop,

        result=f"{crop} is the best crop to be cultivated",

        confidence=round(confidence, 2),

        details=details,

        crop=details,

        top3=top3,

        level=level
    )


SEASONS = {
    "winter": [12, 1, 2],
    "summer": [3, 4, 5],
    "monsoon": [6, 7, 8, 9],
    "post_monson": [10, 11]
}


def get_historical_weather(latitude, longitude, season):

    current_year = date.today().year

    # গত 5 বছরের data
    start_date = f"{current_year - 5}-01-01"
    end_date = f"{current_year - 1}-12-31"

    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_mean,relative_humidity_2m_mean,rain_sum",
        "timezone": "auto"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        if response.status_code != 200:
            print("Weather API Error:", response.status_code)
            return None

        data = response.json()

        daily = data.get("daily")

        if not daily:
            return None

        dates = daily["time"]
        temperatures = daily["temperature_2m_mean"]
        humidity = daily["relative_humidity_2m_mean"]
        rainfall = daily["rain_sum"]

        selected_months = SEASONS.get(season)

        if not selected_months:
            return None

        selected_temperatures = []
        selected_humidity = []
        selected_rainfall = []

        for i, date_string in enumerate(dates):

            month = int(date_string.split("-")[1])

            if month in selected_months:

                if temperatures[i] is not None:
                    selected_temperatures.append(
                        temperatures[i]
                    )

                if humidity[i] is not None:
                    selected_humidity.append(
                        humidity[i]
                    )

                if rainfall[i] is not None:
                    selected_rainfall.append(
                        rainfall[i]
                    )

        if not selected_temperatures:
            return None

        avg_temperature = (
            sum(selected_temperatures)
            / len(selected_temperatures)
        )

        avg_humidity = (
            sum(selected_humidity)
            / len(selected_humidity)
        )

        avg_rainfall = (
            sum(selected_rainfall)
            / len(selected_rainfall)
        )

        return (
            round(avg_temperature, 2),
            round(avg_humidity, 2),
            round(avg_rainfall, 2)
        )

    except Exception as e:

        print("Historical weather error:", e)

        return None


def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if "results" not in data or not data["results"]:
        return None

    result = data["results"][0]

    return (
        result["latitude"],
        result["longitude"],
        result["name"]
    )


def get_historical_rainfall(latitude, longitude, season):

    current_year = date.today().year

    # গত 5 সম্পূর্ণ বছরের data
    start_date = f"{current_year - 5}-01-01"
    end_date = f"{current_year - 1}-12-31"

    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "rain_sum",
        "timezone": "auto"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        if response.status_code != 200:
            print("Rainfall API Error:", response.status_code)
            return None

        data = response.json()

        daily = data.get("daily")

        if not daily:
            return None

        dates = daily["time"]
        rainfall = daily["rain_sum"]

        selected_months = SEASONS.get(season)

        if not selected_months:
            return None

        # প্রতি বছরের selected season-এর total rainfall
        yearly_rainfall = {}

        for i, date_string in enumerate(dates):

            year = int(date_string.split("-")[0])
            month = int(date_string.split("-")[1])

            # শুধু selected season
            if month not in selected_months:
                continue

            if rainfall[i] is not None:

                if year not in yearly_rainfall:
                    yearly_rainfall[year] = 0

                yearly_rainfall[year] += rainfall[i]

        if not yearly_rainfall:
            return None

        # 5 বছরের seasonal rainfall
        rainfall_values = list(
            yearly_rainfall.values()
        )

        five_year_average = (
            sum(rainfall_values)
            / len(rainfall_values)
        )

        return round(five_year_average, 2)

    except Exception as e:

        print("Historical rainfall error:", e)

        return None


@app.route("/weather", methods=["POST"])
def weather():

    city = request.form["city"]
    season = request.form["season"]

    # City → latitude + longitude
    location = get_coordinates(city)

    if location is None:
        return jsonify({
            "success": False,
            "message": "City not found"
        })

    latitude, longitude, city_name = location

    # তোমার existing weather system
    weather = get_weather(city)

    if weather is None:
        return jsonify({
            "success": False,
            "message": "Current weather data পাওয়া যায়নি"
        })

    # Temperature + Humidity আগের মতোই
    temperature, humidity, current_rainfall = weather

    # নতুন 5-year historical rainfall
    historical_rainfall = get_historical_rainfall(
        latitude,
        longitude,
        season
    )

    if historical_rainfall is None:
        return jsonify({
            "success": False,
            "message": "Historical rainfall data পাওয়া যায়নি"
        })

    return jsonify({
        "success": True,
        "city": city_name,
        "season": season,
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": historical_rainfall
    })


if __name__ == "__main__":
    app.run(debug=True)