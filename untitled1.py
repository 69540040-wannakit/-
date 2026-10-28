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
            <p class="text-sm text-stone-500 mt-1">วางแผนโภชนาการและการออกกำลังกายส่วนบุคคลด้วย AI</p>
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
                            <input type="checkbox" value="คาร์บต่ำ (Low Carb)" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 hover:bg-stone-100 transition">
                                🥗 คาร์บต่ำ (Low Carb)
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="โปรตีนสูง (High Protein)" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 hover:bg-stone-100 transition">
                                🥩 โปรตีนสูง (High Protein)
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="มังสวิรัติ (Vegetarian)" class="peer sr-only dietary-checkbox">
                            <div class="px-4 py-2 bg-stone-50 border border-stone-200 rounded-full text-sm text-stone-600 peer-checked:bg-emerald-50 peer-checked:border-emerald-500 peer-checked:text-emerald-700 hover:bg-stone-100 transition">
                                🌱 มังสวิรัติ (Vegetarian)
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="คีโต (Ketogenic)" class="peer sr-only dietary-checkbox">
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

                <button type="submit" id="submitBtn" class="w-full bg-emerald-700 hover:bg-emerald-800 text-white font-medium py-2.5 rounded-xl transition duration-200 shadow-sm flex items-center justify-center gap-2 mt-4 cursor-pointer">
                    <span id="btnText">คำนวณ BMI และสร้างตารางด้วย AI</span>
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
            <p class="text-sm text-stone-500 mt-3">กำลังให้ AI ออกแบบแผนโภชนาการและออกกำลังกาย...</p>
        </div>

        <!-- การ์ดแสดงผลเรียงต่อกันหลายคอลัมน์ -->
        <div id="planContainer" class="grid grid-cols-1 xl:grid-cols-2 gap-6"></div>
    </div>

    <script>
        // Calculate BMI & Gender Condition Logic
        function calculateBMI(weight, heightCM, gender) {
            const heightM = heightCM / 100;
            const bmi = (weight / (heightM * heightM)).toFixed(1);
            let status = '';
            let colorClass = '';

            if (gender === 'male') {
                if (bmi < 18.5) {
                    status = 'น้ำหนักน้อย / ผอม (Underweight)';
                    colorClass = 'bg-blue-50 text-blue-800 border-blue-200';
                } else if (bmi <= 22.9) {
                    status = 'น้ำหนักปกติ / สมส่วน (Normal)';
                    colorClass = 'bg-emerald-50 text-emerald-800 border-emerald-200';
                } else {
                    status = 'น้ำหนักเกิน / อ้วน (Overweight)';
                    colorClass = 'bg-amber-50 text-amber-800 border-amber-200';
                }
            } else { // female
                if (bmi < 18.5) {
                    status = 'น้ำหนักน้อย / ผอม (Underweight)';
                    colorClass = 'bg-blue-50 text-blue-800 border-blue-200';
                } else if (bmi <= 21.9) {
                    status = 'น้ำหนักปกติ / สมส่วน (Normal)';
                    colorClass = 'bg-emerald-50 text-emerald-800 border-emerald-200';
                } else {
                    status = 'น้ำหนักเกิน / อ้วน (Overweight)';
                    colorClass = 'bg-amber-50 text-amber-800 border-amber-200';
                }
            }

            return { bmi, status, colorClass };
        }

        // Mock/Fetch AI API Response
        async function fetchPlanFromAI(gender, weight, height, goal, days, bmi, status, dietaryText) {
            const prompt = `ผู้ใช้เพศ: ${gender === 'male' ? 'ชาย' : 'หญิง'}, น้ำหนัก: ${weight} kg, ส่วนสูง: ${height} cm, ค่า BMI: ${bmi} (${status}), เป้าหมาย: ${goal}
${dietaryText}
กรุณาสร้างแผนโภชนาการและการออกกำลังกายแบบรายวัน จำนวนทั้งหมด ${days} วัน

ตอบกลับเป็น JSON รูปแบบนี้เท่านั้น (ห้ามใส่ markdown หรือโค้ดบล็อก):
[
  {
    "day": 1,
    "title": "วันที่ 1: ชื่อเน้นย้ำเป้าหมาย",
    "meals": {
      "breakfast": "เมนูเช้า",
      "lunch": "เมนูกลางวัน",
      "dinner": "เมนูเย็น"
    },
    "workout": {
      "title": "ชื่อโปรแกรมออกกำลังกาย",
      "detail": "รายละเอียดท่าออกกำลังกายและระยะเวลา"
    }
  }
]`;

            try {
                if (window.gempix && typeof window.gempix.generateText === 'function') {
                    const response = await window.gempix.generateText({ prompt });
                    const cleanText = response.replace(/```json/g, '').replace(/```/g, '').trim();
                    return JSON.parse(cleanText);
                }
            } catch (e) {
                console.warn("AI API call failed or not available, generating fallback structure.", e);
            }

            // Fallback generation for demo/standard loop
            const result = [];
            for (let i = 1; i <= days; i++) {
                result.push({
                    day: i,
                    title: `วันที่ ${i}: แผนสุขภาพสร้างสมดุล (${goal})`,
                    meals: {
                        breakfast: goal === 'เพิ่มกล้ามเนื้อ' ? 'ไข่ต้ม 3 ฟอง + ขนมปังโฮลวีต 2 แผ่น + นมสด' : 'อกไก่ต้ม + กาแฟดำไม่ใส่น้ำตาล',
                        lunch: goal === 'เพิ่มกล้ามเนื้อ' ? 'ข้าวกล้อง + อกไก่ย่าง 200g + ผักต้ม' : 'เกาเหลาอกไก่พิเศษผัก + ข้าวกล้องครึ่งทัพพี',
                        dinner: goal === 'เพิ่มกล้ามเนื้อ' ? 'สเต๊กปลาแซลมอน + มันหวาน + สลัดผัก' : 'สลัดอกไก่ + ไข่ต้ม 1 ฟอง (น้ำสลัดใส)'
                    },
                    workout: {
                        title: goal === 'เพิ่มกล้ามเนื้อ' ? 'เวทเทรนนิ่ง เน้นกล้ามเนื้อใหญ่' : 'คาร์ดิโอ + เวทเทรนนิ่งเบาๆ',
                        detail: goal === 'เพิ่มกล้ามเนื้อ' ? 'Squat, Push-up, Lunge อย่างละ 4 เซต เซตละ 12 ครั้ง' : 'เดินเร็ว/วิ่งเหยาะๆ 30 นาที + สแควท 3 เซต'
                    }
                });
            }
            return result;
        }

        // Render Cards (Loop)
        function renderPlan(planData) {
            const container = document.getElementById('planContainer');
            container.innerHTML = ''; // ล้างตารางเก่าก่อนวาดใหม่เสมอ

            planData.forEach(item => {
                const card = document.createElement('div');
                card.className = 'bg-white rounded-2xl p-6 border border-stone-200/80 shadow-sm hover:shadow-md transition flex flex-col justify-between';
                card.innerHTML = `
                    <div>
                        <div class="flex items-center justify-between mb-4 pb-3 border-b border-stone-100">
                            <h3 class="font-medium text-stone-900">${item.title}</h3>
                            <span class="text-xs bg-stone-100 text-stone-600 px-2.5 py-1 rounded-full font-medium">Day ${item.day}</span>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <!-- Meals -->
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
                            <!-- Workout -->
                            <div>
                                <h4 class="text-xs font-semibold uppercase tracking-wider text-stone-700 mb-3 flex items-center gap-1.5">
                                    🏃‍♂️ การออกกำลังกาย
                                </h4>
                                <div class="bg-stone-50 p-3.5 rounded-xl text-sm h-full flex flex-col justify-center">
                                    <strong class="text-stone-800 block mb-1">${item.workout.title}</strong>
                                    <p class="text-stone-600 text-xs leading-relaxed">${item.workout.detail}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        // Event Listener (รองรับการกดคำนวณซ้ำหลายๆ ครั้งได้)
        document.getElementById('healthForm').addEventListener('submit', async (e) => {
            e.preventDefault();

            const submitBtn = document.getElementById('submitBtn');
            const btnText = document.getElementById('btnText');
            
            // ป้องกันการกดซ้ำระหว่างคำนวณ
            submitBtn.disabled = true;
            submitBtn.classList.add('opacity-75', 'cursor-not-allowed');
            btnText.textContent = 'กำลังประมวลผล...';

            try {
                const gender = document.getElementById('gender').value;
                const weight = parseFloat(document.getElementById('weight').value);
                const height = parseFloat(document.getElementById('height').value);
                const goal = document.getElementById('goal').value;
                const days = parseInt(document.getElementById('days').value) || 7;

                // ดึงข้อมูลข้อจำกัดด้านอาหาร
                const dietaryCheckboxes = document.querySelectorAll('.dietary-checkbox:checked');
                const dietaryPreferences = Array.from(dietaryCheckboxes).map(cb => cb.value).join(', ');
                const dietaryText = dietaryPreferences ? `ข้อจำกัดด้านอาหาร / รูปแบบการทาน: ${dietaryPreferences}` : 'ไม่มีข้อจำกัดด้านอาหาร';

                // 1. Calculate & Display BMI
                const bmiInfo = calculateBMI(weight, height, gender);
                const bmiBanner = document.getElementById('bmiResult');

                document.getElementById('bmiValue').textContent = bmiInfo.bmi;
                document.getElementById('bmiStatusText').textContent = bmiInfo.status;
                bmiBanner.className = `mt-6 p-4 rounded-xl border transition-all ${bmiInfo.colorClass}`;
                bmiBanner.classList.remove('hidden');

                // 2. Fetch AI & Render Plan
                document.getElementById('loading').classList.remove('hidden');
                document.getElementById('planContainer').innerHTML = ''; // ล้างของเก่าออก

                const plan = await fetchPlanFromAI(gender, weight, height, goal, days, bmiInfo.bmi, bmiInfo.status, dietaryText);

                document.getElementById('loading').classList.add('hidden');
                renderPlan(plan);

            } catch (error) {
                console.error("เกิดข้อผิดพลาดในการคำนวณ:", error);
                alert("เกิดข้อผิดพลาดในการสร้างแผน กรุณาลองใหม่อีกครั้ง");
            } finally {
                // คืนค่าปุ่มให้กดคำนวณใหม่ซ้ำได้เสมอ
                submitBtn.disabled = false;
                submitBtn.classList.remove('opacity-75', 'cursor-not-allowed');
                btnText.textContent = 'คำนวณ BMI และสร้างตารางด้วย AI';
            }
        });
    </script>
</body>
</html>
"""

# คำสั่งแสดงผล HTML บน Streamlit
components.html(html_code, height=1200, scrolling=True)
