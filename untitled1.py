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
            <form id="healthForm" class="space-y-5">
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
                        <option value="เพิ่มกล้ามเนื้อ">เพิ่มกล้ามเนื้อ / เพิ่มน้ำหนัก (Muscle Gain)</option>
                        <option value="รักษาน้ำหนักและสุขภาพ">รักษาสุขภาพ / รักษาน้ำหนัก (Maintenance)</option>
                    </select>
                </div>

                <!-- Dietary Preferences -->
                <div>
                    <label class="block text-xs font-medium text-stone-600 mb-2">ข้อจำกัดด้านอาหาร / รูปแบบการทาน (Dietary Preferences)</label>
                    <div class="flex flex-wrap gap-2">
                        <label class="cursor-pointer">
                            <input type="checkbox" value="คาร์บต่ำ" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 hover:bg-stone-100 transition">
                                🥗 คาร์บต่ำ (Low Carb)
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="โปรตีนสูง" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 hover:bg-stone-100 transition">
                                🥩 โปรตีนสูง (High Protein)
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="มังสวิรัติ" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 hover:bg-stone-100 transition">
                                🌱 มังสวิรัติ (Vegetarian)
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="คีโต" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 hover:bg-stone-100 transition">
                                🥑 คีโต (Ketogenic)
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="แพ้ถั่ว" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-red-50 peer-checked:border-red-500 peer-checked:text-red-700 hover:bg-stone-100 transition">
                                🚫 แพ้ถั่ว
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="ไม่ทานอาหารทะเล" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-red-50 peer-checked:border-red-500 peer-checked:text-red-700 hover:bg-stone-100 transition">
                                🚫 ไม่ทานอาหารทะเล
                            </div>
                        </label>
                    </div>
                </div>

                <button type="submit" id="submitBtn" class="w-full bg-emerald-700 hover:bg-emerald-800 text-white font-medium py-2.5 rounded-xl transition duration-200 shadow-sm flex items-center justify-center gap-2 mt-4">
                    <span>คำนวณ BMI และสร้างตารางด้วย AI</span>
                </button>
            </form>

            <!-- BMI Result Banner -->
            <div id="bmiResult" class="hidden mt-6 p-4 rounded-xl border transition-all">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <div>
                        <span class="text-xs uppercase tracking-wider font-semibold opacity-75">สถานะสุขภาพของคุณ</span>
                        <h3 id="bmiStatusText" class="text-lg font-medium">--</h3>
                    </div>
                    <div class="text-right">
                        <span class="text-xs opacity-75 block">ค่า BMI</span>
                        <span id="bmiValue" class="text-2xl font-semibold">--</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Dynamic Results Section -->
        <div id="loading" class="hidden text-center py-12">
            <div class="inline-block animate-spin rounded-full h-8 w-8 border-2 border-emerald-600 border-t-transparent"></div>
            <p class="text-sm text-stone-500 mt-3">กำลังประมวลผลแผนโภชนาการและการออกกำลังกาย...</p>
        </div>

        <!-- การ์ดแสดงผล -->
        <div id="planContainer" class="grid grid-cols-1 xl:grid-cols-2 gap-6"></div>
    </div>

    <script>
        // Calculate BMI
        function calculateBMI(weight, heightCM, gender) {
            const heightM = heightCM / 100;
            const bmi = (weight / (heightM * heightM)).toFixed(1);
            let status = '';
            let colorClass = '';

            const thresholds = gender === 'male' ? { low: 18.5, high: 22.9 } : { low: 18.5, high: 21.9 };

            if (bmi < thresholds.low) {
                status = 'น้ำหนักน้อย / ผอม (Underweight)';
                colorClass = 'bg-blue-50 text-blue-800 border-blue-200';
            } else if (bmi <= thresholds.high) {
                status = 'น้ำหนักปกติ / สมส่วน (Normal)';
                colorClass = 'bg-emerald-50 text-emerald-800 border-emerald-200';
            } else {
                status = 'น้ำหนักเกิน / อ้วน (Overweight)';
                colorClass = 'bg-amber-50 text-amber-800 border-amber-200';
            }
            return { bmi, status, colorClass };
        }

        // Mock/Fetch AI API Response 
        async function fetchPlanFromAI(gender, weight, height, goal, days, bmi, status, dietaryText) {
            
            // 1. Prompt สำหรับการเรียก AI จริง (ครอบคลุมความหลากหลายและข้อจำกัดทั้งหมด)
            const prompt = `ผู้ใช้เพศ: ${gender === 'male' ? 'ชาย' : 'หญิง'}, น้ำหนัก: ${weight} kg, ส่วนสูง: ${height} cm, ค่า BMI: ${bmi} (${status}), เป้าหมาย: ${goal}
ข้อจำกัดด้านอาหาร: ${dietaryText} 

คำสั่งสำคัญ: 
- จัดเมนูให้ถูกต้องตามข้อจำกัดอย่างเคร่งครัด (เช่น มังสวิรัติห้ามมีเนื้อสัตว์/น้ำปลา, คีโตห้ามมีข้าว/น้ำตาล/แป้ง, แพ้ถั่วห้ามมีถั่วทุกชนิด, ไม่ทานอาหารทะเลห้ามมีกุ้งหอยปูปลาน้ำปลา)
- **ต้องมีความหลากหลายของเมนูอาหาร** เมนูในแต่ละวันห้ามซ้ำซากจำเจ สลับสับเปลี่ยนประเภทวัตถุดิบ
- หากเป้าหมายคือ 'เพิ่มกล้ามเนื้อ' หรือ 'โปรตีนสูง' ให้เพิ่มปริมาณโปรตีนในมื้ออาหารให้ชัดเจน

ตอบกลับเป็น JSON รูปแบบนี้เท่านั้น:
[
  {
    "day": 1,
    "title": "วันที่ 1: ชื่อเน้นย้ำเป้าหมาย",
    "meals": { "breakfast": "...", "lunch": "...", "dinner": "..." },
    "workout": { "title": "...", "detail": "..." }
  }
]`;

            try {
                if (window.gempix && typeof window.gempix.generateText === 'function') {
                    const response = await window.gempix.generateText({ prompt });
                    const cleanText = response.replace(/```json/g, '').replace(/```/g, '').trim();
                    return JSON.parse(cleanText);
                }
            } catch (e) {
                console.warn("AI API ไม่พร้อมใช้งาน, ระบบจะใช้ Fallback แผนอาหารที่หลากหลายแทน", e);
            }

            // 2. ระบบ Fallback แบบใหม่: ฐานข้อมูลเมนูแบบหลากหลาย พร้อมระบบ Filter
            
            const isVeg = dietaryText.includes("มังสวิรัติ");
            const isKeto = dietaryText.includes("คีโต") || dietaryText.includes("คาร์บต่ำ");
            const isNoSeafood = dietaryText.includes("ไม่ทานอาหารทะเล");
            const isNutFree = dietaryText.includes("แพ้ถั่ว");
            const isHighProtein = dietaryText.includes("โปรตีนสูง") || goal === 'เพิ่มกล้ามเนื้อ';

            // ฐานข้อมูล Mock Menu แบ่งตามหมวดหมู่และ Tag
            const dbMeals = {
                breakfast: [
                    { name: 'ไข่ต้ม 3 ฟอง + ขนมปังโฮลวีต', veg: false, keto: false, seafood: false, nut: false },
                    { name: 'สลัดอะโวคาโดไข่ต้มน้ำมันมะกอก', veg: true, keto: true, seafood: false, nut: false },
                    { name: 'ข้าวต้มปลาแซลมอนโรยขิง', veg: false, keto: false, seafood: true, nut: false },
                    { name: 'เต้าหู้ผัดเห็ดหอม + กาแฟดำ', veg: true, keto: true, seafood: false, nut: false },
                    { name: 'อกไก่ต้ม + นมอัลมอนด์', veg: false, keto: true, seafood: false, nut: true },
                    { name: 'แซนวิชทูน่าโฮลวีต', veg: false, keto: false, seafood: true, nut: false },
                    { name: 'ข้าวโอ๊ตต้มธัญพืชรวม', veg: true, keto: false, seafood: false, nut: true },
                    { name: 'กรีกโยเกิร์ต + ผลไม้ตระกูลเบอร์รี่', veg: true, keto: false, seafood: false, nut: false },
                    { name: 'ไข่กระทะ (ไม่ใช้น้ำมัน) + ผักต้ม', veg: true, keto: true, seafood: false, nut: false },
                    { name: 'สมูทตี้โปรตีน + กล้วยหอม', veg: true, keto: false, seafood: false, nut: false }
                ],
                lunch: [
                    { name: 'ข้าวกล้อง + อกไก่ย่างพริกไทยดำ + ผักต้ม', veg: false, keto: false, seafood: false, nut: false },
                    { name: 'สลัดปลาแซลมอนย่าง', veg: false, keto: true, seafood: true, nut: false },
                    { name: 'เกาเหลาเต้าหู้เห็ดรวมน้ำใส', veg: true, keto: true, seafood: false, nut: false },
                    { name: 'ข้าวกล้อง + เทมเป้ย่างซีอิ๊ว', veg: true, keto: false, seafood: false, nut: false },
                    { name: 'ผัดกะเพราไก่สับ (ไม่ใส่น้ำตาล) + ไข่ดาว', veg: false, keto: true, seafood: false, nut: false },
                    { name: 'สลัดกุ้งต้ม + อะโวคาโด', veg: false, keto: true, seafood: true, nut: false },
                    { name: 'ควินัวผัดผักรวม + เต้าหู้', veg: true, keto: false, seafood: false, nut: false },
                    { name: 'เส้นบุกผัดขี้เมาไก่', veg: false, keto: true, seafood: false, nut: false },
                    { name: 'ยำวุ้นเส้นเห็ดรวม', veg: true, keto: false, seafood: false, nut: false },
                    { name: 'สเต๊กไก่สไปซี่ + บรอกโคลี', veg: false, keto: true, seafood: false, nut: false }
                ],
                dinner: [
                    { name: 'สเต๊กปลาแซลมอน + สลัดผัก', veg: false, keto: true, seafood: true, nut: false },
                    { name: 'สลัดผักรวมเต้าหู้ย่าง', veg: true, keto: true, seafood: false, nut: false },
                    { name: 'อกไก่ฉีก + ผักสลัด + น้ำสลัดงาใส', veg: false, keto: true, seafood: false, nut: false },
                    { name: 'ต้มยำกุ้งน้ำใส (ไม่ใส่น้ำตาล)', veg: false, keto: true, seafood: true, nut: false },
                    { name: 'ผัดผักบุ้งเต้าเจี้ยว + ข้าวกล้อง', veg: true, keto: false, seafood: false, nut: false },
                    { name: 'ปลากะพงนึ่งมะนาว + ผักลวก', veg: false, keto: true, seafood: true, nut: false },
                    { name: 'ซุปฟักทองใส + ขนมปังโฮลวีต', veg: true, keto: false, seafood: false, nut: false },
                    { name: 'เห็ดย่างเกลือ + สลัดผักใบเขียว', veg: true, keto: true, seafood: false, nut: false },
                    { name: 'สเต๊กเนื้อสันใน + แอสพารากัส', veg: false, keto: true, seafood: false, nut: false },
                    { name: 'แกงจืดเต้าหู้หมูสับ', veg: false, keto: false, seafood: false, nut: false }
                ]
            };

            // ฟังก์ชันกรองอาหารตามข้อจำกัด
            const filterMenu = (menuList) => {
                let filtered = menuList.filter(m => {
                    if (isVeg && !m.veg) return false;
                    if (isKeto && !m.keto) return false;
                    if (isNoSeafood && m.seafood) return false;
                    if (isNutFree && m.nut) return false;
                    return true;
                });
                // หากกรองแล้วไม่เหลืออะไรเลย ให้แสดงเมนู Safe Zone ที่ทานได้ทุกกลุ่ม
                if(filtered.length === 0) {
                    filtered = [{ name: 'สลัดผักออร์แกนิกน้ำใส + เต้าหู้ต้ม (Safe Menu)' }];
                }
                return filtered;
            };

            const availBreakfast = filterMenu(dbMeals.breakfast);
            const availLunch = filterMenu(dbMeals.lunch);
            const availDinner = filterMenu(dbMeals.dinner);

            const result = [];
            for (let i = 1; i <= days; i++) {
                
                // ใช้ Modulo (การหารเอาเศษ) เพื่อหมุนเวียนเมนูไม่ให้ซ้ำติดกัน
                let b = availBreakfast[(i-1) % availBreakfast.length].name;
                let l = availLunch[(i-1) % availLunch.length].name;
                let d = availDinner[(i-1) % availDinner.length].name;

                // เพิ่มโน้ตสำหรับเป้าหมายโปรตีนสูง
                if (isHighProtein) {
                    b += ' (เพิ่มไข่ต้ม/โปรตีนเสริม)';
                    l += ' (เพิ่มปริมาณเนื้อสัตว์/เต้าหู้ 1.5 เท่า)';
                    d += ' (เสริมโปรตีน 1 ส่วน)';
                }

                // กำหนดแผนออกกำลังกาย
                let workoutTitle, workoutDetail;
                if (goal === 'ลดน้ำหนัก') {
                    workoutTitle = 'คาร์ดิโอเผาผลาญไขมัน';
                    workoutDetail = 'เดินเร็ว/จ็อกกิ้ง 45 นาที + ยืดเหยียดร่างกาย 10 นาที';
                } else if (goal === 'เพิ่มกล้ามเนื้อ') {
                    workoutTitle = 'เวทเทรนนิ่ง เน้นสร้างกล้ามเนื้อ';
                    workoutDetail = 'Squat, Push-up, Lunge อย่างละ 4 เซต เซตละ 12 ครั้ง พักระหว่างเซต 60 วินาที';
                } else {
                    workoutTitle = 'ออกกำลังกายเพื่อสุขภาพองค์รวม';
                    workoutDetail = 'โยคะ 30 นาที สลับกับการเดินเล่นรับอากาศบริสุทธิ์ 20 นาที';
                }

                result.push({
                    day: i,
                    title: `วันที่ ${i}: ${goal} อย่างยั่งยืน`,
                    meals: { breakfast: b, lunch: l, dinner: d },
                    workout: { title: workoutTitle, detail: workoutDetail }
                });
            }
            return result;
        }

        // Render Cards
        function renderPlan(planData) {
            const container = document.getElementById('planContainer');
            container.innerHTML = '';

            planData.forEach(item => {
                const card = document.createElement('div');
                card.className = 'bg-white rounded-2xl p-6 border border-stone-200/80 shadow-sm hover:shadow-md transition h-full';
                card.innerHTML = `
                    <div class="flex items-center justify-between mb-4 pb-3 border-b border-stone-100">
                        <h3 class="font-medium text-stone-900">${item.title}</h3>
                        <span class="text-xs bg-stone-100 text-stone-600 px-2.5 py-1 rounded-full font-medium">Day ${item.day}</span>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 h-[calc(100%-3rem)]">
                        <div>
                            <h4 class="text-xs font-semibold uppercase tracking-wider text-emerald-700 mb-3 flex items-center gap-1.5">
                                🍳 ตารางอาหาร
                            </h4>
                            <ul class="space-y-2 text-sm text-stone-600">
                                <li class="bg-stone-50 p-2.5 rounded-xl"><strong class="text-stone-800">มื้อเช้า:</strong> ${item.meals.breakfast}</li>
                                <li class="bg-stone-50 p-2.5 rounded-xl"><strong class="text-stone-800">มื้อกลางวัน:</strong> ${item.meals.lunch}</li>
                                <li class="bg-stone-50 p-2.5 rounded-xl"><strong class="text-stone-800">มื้อเย็น:</strong> ${item.meals.dinner}</li>
                            </ul>
                        </div>
                        <div>
                            <h4 class="text-xs font-semibold uppercase tracking-wider text-stone-700 mb-3 flex items-center gap-1.5">
                                🏃‍♂️ การออกกำลังกาย
                            </h4>
                            <div class="bg-stone-50 p-3.5 rounded-xl text-sm h-[calc(100%-2rem)] flex flex-col justify-center">
                                <strong class="text-stone-800 block mb-1">${item.workout.title}</strong>
                                <p class="text-stone-600 text-xs leading-relaxed">${item.workout.detail}</p>
                            </div>
                        </div>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        // Event Listener
        document.getElementById('healthForm').addEventListener('submit', async (e) => {
            e.preventDefault();

            const gender = document.getElementById('gender').value;
            const weight = parseFloat(document.getElementById('weight').value);
            const height = parseFloat(document.getElementById('height').value);
            const goal = document.getElementById('goal').value;
            const days = parseInt(document.getElementById('days').value) || 7;

            const dietaryCheckboxes = document.querySelectorAll('.dietary-checkbox:checked');
            const dietaryPreferences = Array.from(dietaryCheckboxes).map(cb => cb.value).join(', ');
            const dietaryText = dietaryPreferences ? dietaryPreferences : 'ไม่มีข้อจำกัดด้านอาหาร';

            // 1. BMI
            const bmiInfo = calculateBMI(weight, height, gender);
            const bmiBanner = document.getElementById('bmiResult');
            document.getElementById('bmiValue').textContent = bmiInfo.bmi;
            document.getElementById('bmiStatusText').textContent = bmiInfo.status;
            bmiBanner.className = `mt-6 p-4 rounded-xl border transition-all ${bmiInfo.colorClass}`;
            bmiBanner.classList.remove('hidden');

            // 2. Fetch Plan
            document.getElementById('loading').classList.remove('hidden');
            document.getElementById('planContainer').innerHTML = '';

            const plan = await fetchPlanFromAI(gender, weight, height, goal, days, bmiInfo.bmi, bmiInfo.status, dietaryText);

            document.getElementById('loading').classList.add('hidden');
            renderPlan(plan);
        });
    </script>
</body>
</html>
"""

components.html(html_code, height=1200, scrolling=True)
