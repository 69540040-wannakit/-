# -*- coding: utf-8 -*-

import streamlit as st
import streamlit.components.v1 as components

# 1. เพิ่มคำสั่งนี้เป็นบรรทัดแรกของ Streamlit เพื่อให้แสดงผลแบบกว้าง (Wide Layout) เต็มหน้าจอ
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
    <!-- 2. เปลี่ยนจาก max-w-4xl เป็น w-full และเพิ่ม padding ด้านข้างให้เต็มหน้าจอ -->
    <div class="w-full px-4 md:px-12 py-8">
        <!-- Header -->
        <header class="text-center mb-8">
            <h1 class="text-3xl font-light text-stone-900 mt-2">Health & Meal Planner</h1>
            <p class="text-sm text-stone-500 mt-1">วางแผนโภชนาการและการออกกำลังกายส่วนบุคคลด้วย AI</p>
        </header>

        <!-- BMI Reference Table -->
        <div class="bg-white rounded-2xl p-5 border border-stone-200/80 shadow-sm mb-6 max-w-6xl mx-auto">
            <h2 class="text-sm font-medium text-stone-700 mb-3 flex items-center gap-2">
                <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.0
