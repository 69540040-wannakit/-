# -*- coding: utf-8 -*-

import streamlit as st
import streamlit.components.v1 as components

# 1. แสดงผลแบบกว้าง (Wide Layout) เต็มหน้าจอ
st.set_page_config(page_title="Health & Meal Planner", layout="wide")

# วางโค้ด HTML ทั้งหมดไว้ด้านล่างนี้
html_code = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health & Meal Planner</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Kanit', sans-serif; }
    </style>
</head>
<body class="bg-stone-50 text-stone-800 min-h-screen pb-12">
    <div class="w-full px-4 md:px-12 py-8">
        <!-- Header -->
        <header class="text-center mb-8">
            <h1 class="text-3xl font-light text-stone-900 mt-2">Health & Meal Planner</h1>
        </header>

        <!-- BMI Reference Table -->
        <div class="bg-white rounded-2xl p-5 border border-stone-200/80 shadow-sm mb-6 max-w-6xl mx-auto">
            <h2 class="text-sm font-medium text-stone-700 mb-3 flex items-center gap-2">
                <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                ตารางเกณฑ์ค่า BMI อ้างอิง (ชาย & หญิง)
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <!-- Male -->
                <div class="bg-stone-50 p-3 rounded-xl border border-stone-100">
                    <span class="font-semibold text-stone-700 block mb-2">👨🏼‍💼 เพศชาย</span>
                    <ul class="space-y-1 text-stone-600">
                        <li class="flex justify-between"><span>ผอม (Underweight):</span> <span class="font-medium text-blue-600">&lt; 18.5</span></li>
                        <li class="flex justify-between"><span>น้ำหนักปกติ (Normal):</span> <span class="font-medium text-emerald-600">18.5 - 22.9</span></li>
                        <li class="flex justify-between"><span>น้ำหนักเกิน/อ้วน (Overweight):</span> <span class="font-medium text-amber-600">≥ 23.0</span></li>
                    </ul>
                </div>
                <!-- Female -->
                <div class="bg-stone-50 p-3 rounded-xl border border-stone-100">
                    <span class="font-semibold text-stone-700 block mb-2">👩🏼‍💼 เพศหญิง</span>
                    <ul class="space-y-1 text-stone-600">
                        <li class="flex justify-between"><span>ผอม (Underweight):</span> <span class="font-medium text-blue-600">&lt; 18.5</span></li>
                        <li class="flex justify-between"><span>น้ำหนักปกติ (Normal):</span> <span class="font-medium text-emerald-600">18.5 - 21.9</span></li>
                        <li class="flex justify-between"><span>น้ำหนักเกิน/อ้วน (Overweight):</span> <span class="font-medium text-amber-600">≥ 22.0</span></li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Form Section -->
        <div class="bg-white rounded-2xl p-6 border border-stone-200/80 shadow-sm mb-8 max-w-6xl mx-auto">
            <form id="healthForm" class="space-y-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
                    <div>
                        <label class="block text-xs font-medium text-stone-600 mb-1">เพศ</label>
                        <select id="gender" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                            <option value="male">ชาย</option>
                            <option value="female">หญิง</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-stone-600 mb-1">น้ำหนัก (กิโลกรัม)</label>
                        <input type="number" id="weight" placeholder="เช่น 65" required min="20" max="300" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-stone-600 mb-1">ส่วนสูง (เซนติเมตร)</label>
                        <input type="number" id="height" placeholder="เช่น 170" required min="100" max="250" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-stone-600 mb-1">จำนวนวัน (1 - 30 วัน)</label>
                        <input type="number" id="days" value="7" required min="1" max="30" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-medium text-stone-600 mb-1">เป้าหมายสุขภาพ</label>
                    <select id="goal" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                        <option value="ลดน้ำหนัก">ลดน้ำหนัก / กระชับสัดส่วน (Weight Loss)</option>
                        <option value="เพิ่มกล้ามเนื้อ">เพิ่มกล้ามเนื้อ / เพิ่มน้ำหนัก
