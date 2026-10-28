<!DOCTYPE html>
<html lang="th" class="h-full bg-stone-50">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health & Meal Planner - AI วางแผนโภชนาการและการออกกำลังกาย</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Kanit -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Kanit', 'sans-serif'],
                    },
                    colors: {
                        emerald: {
                            50: '#ecfdf5',
                            100: '#d1fae5',
                            500: '#10b981',
                            600: '#059669',
                            700: '#047857',
                            800: '#065f46',
                            900: '#064e3b',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Kanit', sans-serif; }
        /* Custom scrollbar for modern feel */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #f5f5f4; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        @media print {
            .no-print { display: none !important; }
            .print-only { display: block !important; }
            body { background: white; color: black; }
        }
    </style>
</head>
<body class="bg-stone-50 text-stone-800 min-h-screen flex flex-col antialiased">

    <!-- Top Navigation / Banner Header -->
    <header class="bg-white border-b border-stone-200 sticky top-0 z-30 shadow-sm no-print">
        <div class="w-full px-4 sm:px-6 lg:px-10 py-3 flex items-center justify-between flex-wrap gap-4">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-emerald-600 flex items-center justify-center text-white font-bold text-xl shadow-md shadow-emerald-600/20">
                    <i class="fa-solid font-bold fa-heart-pulse"></i>
                </div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight text-stone-900 leading-tight">Health & Meal Planner</h1>
                    <p class="text-xs text-stone-500">วางแผนโภชนาการและการออกกำลังกายระดับมืออาชีพด้วย AI</p>
                </div>
            </div>

            <div class="flex items-center gap-3 text-xs font-medium">
                <button onclick="window.print()" class="px-3 py-2 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-lg flex items-center gap-1.5 transition">
                    <i class="fa-solid fa-print"></i> พิมพ์ / พิมพ์เป็น PDF
                </button>
                <button id="resetAppBtn" class="px-3 py-2 border border-stone-200 text-stone-600 hover:bg-stone-100 rounded-lg flex items-center gap-1.5 transition">
                    <i class="fa-solid fa-rotate-right"></i> รีเซ็ตข้อมูล
                </button>
            </div>
        </div>
    </header>

    <!-- Main Dynamic Content Container (Full Width Responsive Layout) -->
    <main class="w-full px-4 sm:px-6 lg:px-10 py-6 flex-grow">

        <!-- BMI Reference Table Section -->
        <div class="bg-white rounded-2xl p-5 border border-stone-200/80 shadow-sm mb-6 no-print">
            <div class="flex items-center justify-between mb-3 cursor-pointer" onclick="toggleBMITable()">
                <h2 class="text-sm font-semibold text-stone-800 flex items-center gap-2">
                    <i class="fa-solid fa-circle-info text-emerald-600"></i>
                    เกณฑ์มาตรฐานดัชนีมวลกาย (BMI Reference Table)
                </h2>
                <span class="text-xs text-stone-400 font-normal hover:text-stone-600" id="toggleTableText">ซ่อนข้อมูล <i class="fa-solid fa-chevron-up"></i></span>
            </div>
            
            <div id="bmiTableContent" class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <!-- Male Reference -->
                <div class="bg-blue-50/50 p-4 rounded-xl border border-blue-100">
                    <span class="font-semibold text-blue-900 flex items-center gap-1.5 mb-2.5">
                        <i class="fa-solid fa-mars text-blue-600"></i> เพศชาย (Male Standard)
                    </span>
                    <ul class="space-y-1.5 text-stone-700">
                        <li class="flex justify-between items-center bg-white/70 px-2.5 py-1 rounded">
                            <span>น้ำหนักน้อย / ผอม (Underweight):</span>
                            <span class="font-bold text-blue-600">&lt; 18.5</span>
                        </li>
                        <li class="flex justify-between items-center bg-white/70 px-2.5 py-1 rounded">
                            <span>น้ำหนักปกติ / สมส่วน (Normal):</span>
                            <span class="font-bold text-emerald-600">18.5 - 22.9</span>
                        </li>
                        <li class="flex justify-between items-center bg-white/70 px-2.5 py-1 rounded">
                            <span>น้ำหนักเกิน / อ้วน (Overweight):</span>
                            <span class="font-bold text-amber-600">≥ 23.0</span>
                        </li>
                    </ul>
                </div>
                <!-- Female Reference -->
                <div class="bg-rose-50/50 p-4 rounded-xl border border-rose-100">
                    <span class="font-semibold text-rose-900 flex items-center gap-1.5 mb-2.5">
                        <i class="fa-solid fa-venus text-rose-600"></i> เพศหญิง (Female Standard)
                    </span>
                    <ul class="space-y-1.5 text-stone-700">
                        <li class="flex justify-between items-center bg-white/70 px-2.5 py-1 rounded">
                            <span>น้ำหนักน้อย / ผอม (Underweight):</span>
                            <span class="font-bold text-blue-600">&lt; 18.5</span>
                        </li>
                        <li class="flex justify-between items-center bg-white/70 px-2.5 py-1 rounded">
                            <span>น้ำหนักปกติ / สมส่วน (Normal):</span>
                            <span class="font-bold text-emerald-600">18.5 - 21.9</span>
                        </li>
                        <li class="flex justify-between items-center bg-white/70 px-2.5 py-1 rounded">
                            <span>น้ำหนักเกิน / อ้วน (Overweight):</span>
                            <span class="font-bold text-amber-600">≥ 22.0</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Form Section -->
        <div class="bg-white rounded-2xl p-6 border border-stone-200/80 shadow-sm mb-8 no-print">
            <h2 class="text-base font-semibold text-stone-800 mb-4 flex items-center gap-2">
                <i class="fa-solid fa-sliders text-emerald-600"></i> ข้อมูลส่วนบุคคลและเป้าหมายสุขภาพ
            </h2>

            <form id="healthForm" class="space-y-5">
                <!-- Basic Metrics Row -->
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-4">
                    <div>
                        <label class="block text-xs font-medium text-stone-700 mb-1">เพศ</label>
                        <select id="gender" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                            <option value="male">ชาย (Male)</option>
                            <option value="female">หญิง (Female)</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-xs font-medium text-stone-700 mb-1">อายุ (ปี)</label>
                        <input type="number" id="age" value="28" min="12" max="100" required class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                    </div>

                    <div>
                        <label class="block text-xs font-medium text-stone-700 mb-1">น้ำหนัก (กิโลกรัม)</label>
                        <input type="number" id="weight" value="65" placeholder="เช่น 65" step="0.5" required min="20" max="300" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                    </div>

                    <div>
                        <label class="block text-xs font-medium text-stone-700 mb-1">ส่วนสูง (เซนติเมตร)</label>
                        <input type="number" id="height" value="170" placeholder="เช่น 170" required min="100" max="250" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                    </div>

                    <div>
                        <label class="block text-xs font-medium text-stone-700 mb-1">จำนวนวันที่วางแผน (1-30)</label>
                        <input type="number" id="days" value="7" required min="1" max="30" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                    </div>
                </div>

                <!-- Activity Level & Goal Row -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-medium text-stone-700 mb-1">เป้าหมายสุขภาพ</label>
                        <select id="goal" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                            <option value="ลดน้ำหนัก">ลดน้ำหนัก / กระชับสัดส่วน (Weight Loss - Caloric Deficit)</option>
                            <option value="เพิ่มกล้ามเนื้อ">เพิ่มกล้ามเนื้อ / เพิ่มน้ำหนัก (Muscle Gain - Caloric Surplus)</option>
                            <option value="รักษาน้ำหนักและสุขภาพ">รักษาสุขภาพ / รักษาน้ำหนัก (Maintenance)</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-xs font-medium text-stone-700 mb-1">ระดับกิจกรรมประจำวัน (Activity Level)</label>
                        <select id="activity" class="w-full bg-stone-50 border border-stone-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition">
                            <option value="1.2">นั่งทำงานเป็นหลัก / แทบไม่ได้ออกกำลังกาย (Sedentary)</option>
                            <option value="1.375" selected>ออกกำลังกายเบาๆ 1-3 วัน/สัปดาห์ (Lightly Active)</option>
                            <option value="1.55">ออกกำลังกายปานกลาง 3-5 วัน/สัปดาห์ (Moderately Active)</option>
                            <option value="1.725">ออกกำลังกายหนัก 6-7 วัน/สัปดาห์ (Very Active)</option>
                        </select>
                    </div>
                </div>

                <!-- Dietary Preferences & Restrictions (Interactive Tags) -->
                <div>
                    <label class="block text-xs font-medium text-stone-700 mb-2">ข้อจำกัดด้านอาหาร / รูปแบบการทาน (Dietary Preferences)</label>
                    <div class="flex flex-wrap gap-2 text-xs">
                        <label class="cursor-pointer">
                            <input type="checkbox" value="คาร์บต่ำ (Low Carb)" class="diet-pref hidden peer">
                            <span class="inline-block px-3 py-1.5 rounded-xl border border-stone-200 bg-stone-50 peer-checked:bg-emerald-600 peer-checked:text-white peer-checked:border-emerald-600 transition">🥗 คาร์บต่ำ (Low Carb)</span>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="โปรตีนสูง (High Protein)" class="diet-pref hidden peer" checked>
                            <span class="inline-block px-3 py-1.5 rounded-xl border border-stone-200 bg-stone-50 peer-checked:bg-emerald-600 peer-checked:text-white peer-checked:border-emerald-600 transition">🥩 โปรตีนสูง (High Protein)</span>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="มังสวิรัติ (Vegetarian)" class="diet-pref hidden peer">
                            <span class="inline-block px-3 py-1.5 rounded-xl border border-stone-200 bg-stone-50 peer-checked:bg-emerald-600 peer-checked:text-white peer-checked:border-emerald-600 transition">🌱 มังสวิรัติ (Vegetarian)</span>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="คีโต (Keto)" class="diet-pref hidden peer">
                            <span class="inline-block px-3 py-1.5 rounded-xl border border-stone-200 bg-stone-50 peer-checked:bg-emerald-600 peer-checked:text-white peer-checked:border-emerald-600 transition">🥑 คีโต (Ketogenic)</span>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="ไม่ใส่ถั่ว" class="diet-pref hidden peer">
                            <span class="inline-block px-3 py-1.5 rounded-xl border border-stone-200 bg-stone-50 peer-checked:bg-emerald-600 peer-checked:text-white peer-checked:border-emerald-600 transition">🚫 แพ้ถั่ว</span>
                        </label>
                        <label class="cursor-pointer">
                            <input type="checkbox" value="ไม่ทานอาหารทะเล" class="diet-pref hidden peer">
                            <span class="inline-block px-3 py-1.5 rounded-xl border border-stone-200 bg-stone-50 peer-checked:bg-emerald-600 peer-checked:text-white peer-checked:border-emerald-600 transition">🚫 ไม่ทานอาหารทะเล</span>
                        </label>
                    </div>
                </div>

                <button type="submit" id="submitBtn" class="w-full bg-emerald-700 hover:bg-emerald-800 text-white font-medium py-3 rounded-xl transition duration-200 shadow-md shadow-emerald-700/20 flex items-center justify-center gap-2 text-base">
                    <i class="fa-solid fa-wand-magic-sparkles"></i>
                    <span>คำนวณดัชนีและสร้างตารางโภชนาการด้วย AI</span>
                </button>
            </form>

            <!-- BMI & Energy Analytics Dashboard Banner -->
            <div id="bmiResult" class="hidden mt-6 p-5 rounded-2xl border transition-all">
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 divide-y sm:divide-y-0 sm:divide-x divide-stone-200/60">
                    <div class="pr-2 pt-2 sm:pt-0">
                        <span class="text-xs uppercase tracking-wider font-semibold opacity-75">สถานะ BMI</span>
                        <h3 id="bmiStatusText" class="text-lg font-bold leading-tight mt-0.5">--</h3>
                    </div>
                    <div class="sm:px-4 pt-2 sm:pt-0">
                        <span class="text-xs opacity-75 block">ค่า BMI ของคุณ</span>
                        <div class="flex items-baseline gap-2">
                            <span id="bmiValue" class="text-2xl font-black">--</span>
                            <span class="text-xs font-normal opacity-80">kg/m²</span>
                        </div>
                    </div>
                    <div class="sm:px-4 pt-2 sm:pt-0">
                        <span class="text-xs opacity-75 block">อัตราเผาผลาญพื้นฐาน (BMR)</span>
                        <div class="flex items-baseline gap-1">
                            <span id="bmrValue" class="text-xl font-bold">--</span>
                            <span class="text-xs">kcal/วัน</span>
                        </div>
                    </div>
                    <div class="sm:pl-4 pt-2 sm:pt-0">
                        <span class="text-xs opacity-75 block">พลังงานเป้าหมาย (TDEE Adjusted)</span>
                        <div class="flex items-baseline gap-1">
                            <span id="tdeeValue" class="text-xl font-extrabold text-emerald-700">--</span>
                            <span class="text-xs font-semibold text-emerald-700">kcal/วัน</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Progress Tracking & Day Filters (Shows up after plan is ready) -->
        <div id="planToolbar" class="hidden mb-6 bg-white p-4 rounded-2xl border border-stone-200/80 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4 no-print">
            <!-- Progress Bar -->
            <div class="w-full md:w-1/2">
                <div class="flex justify-between items-center text-xs font-medium text-stone-600 mb-1.5">
                    <span>ความคืบหน้ากิจกรรมทั้งหมด (Progress Tracker)</span>
                    <span id="progressPercent" class="font-bold text-emerald-600">0%</span>
                </div>
                <div class="w-full bg-stone-100 rounded-full h-2.5 overflow-hidden">
                    <div id="progressBar" class="bg-emerald-600 h-2.5 rounded-full transition-all duration-300 w-0"></div>
                </div>
            </div>

            <!-- Search & Filter Bar -->
            <div class="flex items-center gap-2 w-full md:w-auto">
                <div class="relative flex-grow md:flex-grow-0 md:w-64">
                    <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-stone-400 text-xs"></i>
                    <input type="text" id="searchDay" placeholder="ค้นหาเมนู หรือการออกกำลังกาย..." class="w-full pl-8 pr-3 py-1.5 bg-stone-50 border border-stone-200 rounded-xl text-xs focus:outline-none focus:ring-1 focus:ring-emerald-500">
                </div>
                <select id="filterDay" class="bg-stone-50 border border-stone-200 rounded-xl px-3 py-1.5 text-xs focus:outline-none focus:ring-1 focus:ring-emerald-500">
                    <option value="all">แสดงทุกวัน</option>
                    <option value="incomplete">ยังไม่ได้ทำ</option>
                    <option value="completed">เสร็จสิ้นแล้ว</option>
                </select>
            </div>
        </div>

        <!-- Dynamic Results Loading Indicator -->
        <div id="loading" class="hidden text-center py-16 bg-white rounded-2xl border border-stone-200/80 shadow-sm my-6">
            <div class="inline-block animate-spin rounded-full h-10 w-10 border-4 border-emerald-600 border-t-transparent"></div>
            <p class="text-base font-medium text-stone-800 mt-4">กำลังประมวลผลคำนวณแคลอรีและให้ Gemini AI ออกแบบแผนสุขภาพ...</p>
            <p class="text-xs text-stone-400 mt-1">อาจใช้เวลาประมาณ 3-6 วินาที ขึ้นอยู่กับจำนวนวันที่เลือก</p>
        </div>

        <!-- Dynamic Cards Grid (Full Width, Multi-column on Large Screens) -->
        <div id="planContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-6"></div>

        <!-- Empty State Message -->
        <div id="emptyState" class="text-center py-16 bg-white/50 rounded-2xl border border-dashed border-stone-300">
            <i class="fa-solid fa-utensils text-4xl text-stone-300 mb-3"></i>
            <h3 class="text-base font-medium text-stone-600">ยังไม่มีการสร้างแผนสุขภาพ</h3>
            <p class="text-xs text-stone-400 max-w-sm mx-auto mt-1">กรอกข้อมูลส่วนตัว น้ำหนัก ส่วนสูง และเป้าหมายของคุณ จากนั้นกดปุ่ม "คำนวณและสร้างตารางด้วย AI" เพื่อเริ่มต้น</p>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-stone-200 py-4 px-6 text-center text-xs text-stone-400 no-print">
        <p>© Health & Meal Planner AI. ข้อมูลโภชนาการนี้เป็นคำแนะนำทั่วไป ควรปรึกษาแพทย์หรือผู้เชี่ยวชาญก่อนเปลี่ยนพฤติกรรมสุขภาพแบบกะทันหัน</p>
    </footer>

    <!-- App JavaScript Logic -->
    <script>
        // Store Application State
        let currentPlanData = [];

        // Helper: Calculate BMI and categorize based on exact Male/Female standards
        function calculateBMI(weight, heightCM, gender) {
            const heightM = heightCM / 100;
            const bmi = parseFloat((weight / (heightM * heightM)).toFixed(1));
            let status = '';
            let colorClass = '';

            if (gender === 'male') {
                if (bmi < 18.5) {
                    status = 'น้ำหนักน้อย / ผอม (Underweight)';
                    colorClass = 'bg-blue-50 text-blue-900 border-blue-200';
                } else if (bmi <= 22.9) {
                    status = 'น้ำหนักปกติ / สมส่วน (Normal)';
                    colorClass = 'bg-emerald-50 text-emerald-900 border-emerald-200';
                } else {
                    status = 'น้ำหนักเกิน / อ้วน (Overweight)';
                    colorClass = 'bg-amber-50 text-amber-900 border-amber-200';
                }
            } else { // female
                if (bmi < 18.5) {
                    status = 'น้ำหนักน้อย / ผอม (Underweight)';
                    colorClass = 'bg-blue-50 text-blue-900 border-blue-200';
                } else if (bmi <= 21.9) {
                    status = 'น้ำหนักปกติ / สมส่วน (Normal)';
                    colorClass = 'bg-emerald-50 text-emerald-900 border-emerald-200';
                } else {
                    status = 'น้ำหนักเกิน / อ้วน (Overweight)';
                    colorClass = 'bg-amber-50 text-amber-900 border-amber-200';
                }
            }

            return { bmi, status, colorClass };
        }

        // Helper: Calculate BMR (Mifflin-St Jeor Equation) & TDEE
        function calculateEnergy(gender, weight, heightCM, age, activityFactor, goal) {
            let bmr = 0;
            if (gender === 'male') {
                bmr = (10 * weight) + (6.25 * heightCM) - (5 * age) + 5;
            } else {
                bmr = (10 * weight) + (6.25 * heightCM) - (5 * age) - 161;
            }

            let tdee = bmr * parseFloat(activityFactor);

            // Adjust TDEE based on Health Goal
            if (goal === 'ลดน้ำหนัก') {
                tdee -= 400; // Caloric Deficit
            } else if (goal === 'เพิ่มกล้ามเนื้อ') {
                tdee += 350; // Caloric Surplus
            }

            return {
                bmr: Math.round(bmr),
                tdee: Math.round(tdee)
            };
        }

        // Collapsible BMI table toggle
        function toggleBMITable() {
            const content = document.getElementById('bmiTableContent');
            const toggleText = document.getElementById('toggleTableText');
            if (content.classList.contains('hidden')) {
                content.classList.remove('hidden');
                toggleText.innerHTML = 'ซ่อนข้อมูล <i class="fa-solid fa-chevron-up"></i>';
            } else {
                content.classList.add('hidden');
                toggleText.innerHTML = 'แสดงตาราง <i class="fa-solid fa-chevron-down"></i>';
            }
        }

        // Call Gemini API directly for AI plan generation
        async function fetchPlanFromGeminiAPI(gender, weight, height, age, goal, days, bmi, status, tdee, dietPrefs) {
            const apiKey = ""; // Canvas runtime automatically supplies valid key if left empty
            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=${apiKey}`;

            const userPrompt = `โปรดสร้างแผนโภชนาการและการออกกำลังกายแบบรายวันจำนวนทั้งหมด ${days} วัน
ข้อมูลผู้ใช้:
- เพศ: ${gender === 'male' ? 'ชาย' : 'หญิง'}
- น้ำหนัก: ${weight} kg, ส่วนสูง: ${height} cm, อายุ: ${age} ปี
- ค่า BMI: ${bmi} (${status})
- เป้าหมายพลังงานเป้าหมาย (TDEE Target): ${tdee} kcal/วัน
- เป้าหมายหลัก: ${goal}
- ความต้องการโภชนาการเพิ่มเติม: ${dietPrefs.length > 0 ? dietPrefs.join(', ') : 'ไม่มี'}

ข้อกำหนด:
ให้สร้างแผนรายวันทั้ง ${days} วัน คำนวณแคลอรีโดยประมาณให้เหมาะสม ตอบกลับตาม JSON Schema เท่านั้น`;

            const payload = {
                contents: [
                    { parts: [{ text: userPrompt }] }
                ],
                systemInstruction: {
                    parts: [{
                        text: "คุณคือผู้เชี่ยวชาญด้านโภชนาการและการออกกำลังกาย (Nutritional & Fitness Coach) ออกแบบตารางอาหารและออกกำลังกายภาษาไทยให้เหมาะกับคนไทย เข้าถึงวัตถุดิบท้องถิ่นได้ง่าย คำนวณแคลอรีให้สอดคล้องกับเป้าหมายของผู้ใช้ ตอบกลับเป็น JSON Schema เท่านั้น"
                    }]
                },
                generationConfig: {
                    responseMimeType: "application/json",
                    responseSchema: {
                        type: "ARRAY",
                        description: "ตารางแผนโภชนาการและการออกกำลังกายรายวัน",
                        items: {
                            type: "OBJECT",
                            properties: {
                                day: { type: "INTEGER" },
                                title: { type: "STRING" },
                                estCalories: { type: "INTEGER" },
                                meals: {
                                    type: "OBJECT",
                                    properties: {
                                        breakfast: { type: "STRING" },
                                        lunch: { type: "STRING" },
                                        dinner: { type: "STRING" },
                                        snack: { type: "STRING" }
                                    },
                                    required: ["breakfast", "lunch", "dinner"]
                                },
                                workout: {
                                    type: "OBJECT",
                                    properties: {
                                        title: { type: "STRING" },
                                        detail: { type: "STRING" },
                                        durationMinutes: { type: "INTEGER" }
                                    },
                                    required: ["title", "detail"]
                                }
                            },
                            required: ["day", "title", "meals", "workout"]
                        }
                    }
                }
            };

            try {
                // Exponential backoff strategy
                let response;
                let delay = 1000;
                for (let i = 0; i < 3; i++) {
                    try {
                        response = await fetch(apiUrl, {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(payload)
                        });
                        if (response.ok) break;
                    } catch (err) {
                        if (i === 2) throw err;
                    }
                    await new Promise(res => setTimeout(res, delay));
                    delay *= 2;
                }

                if (response && response.ok) {
                    const result = await response.json();
                    const candidate = result.candidates?.[0];
                    if (candidate && candidate.content?.parts?.[0]?.text) {
                        const jsonText = candidate.content.parts[0].text;
                        const parsed = JSON.parse(jsonText);
                        if (Array.isArray(parsed) && parsed.length > 0) {
                            return parsed;
                        }
                    }
                }
            } catch (e) {
                console.warn("Gemini API call failed, switching to local intelligent fallback generator.", e);
            }

            // Fallback Generator if network / key is unavailable
            return generateFallbackPlan(goal, days, tdee, dietPrefs);
        }

        // Fallback Meal & Exercise Data Generator
        function generateFallbackPlan(goal, days, targetTdee, dietPrefs) {
            const plan = [];
            
            const breakfastOptions = [
                "ไข่ต้ม 2 ฟอง + ขนมปังโฮลวีต 2 แผ่น + กาแฟดำ",
                "โจ๊กอกไก่ใส่ไข่ + ผักโรย (น้ำมันน้อย)",
                "ข้าวต้มปลาแซลมอน/กุ้ง + นมถั่วเหลืองสูตรหวานน้อย",
                "กราโนล่า + โยเกิร์ตไขมันต่ำ 0% + ผลไม้ตระกูลเบอร์รี",
                "แซนด์วิชทูน่าในน้ำแร่ + น้ำส้มคั้นสด 1 แก้ว"
            ];

            const lunchOptions = [
                "ข้าวกล้อง 1.5 ทัพพี + อกไก่ผัดขิง + ผักต้ม",
                "เกาเหลาอกไก่พิเศษผัก (ไม่เจียวกระเทียม) + ข้าวสองสี",
                "สเต๊กปลาปลากะพงย่าง + มันหวานนึ่ง + สลัดผักน้ำใส",
                "ส้มตำไทย (หวานน้อย) + ไก่ย่างลอกหนัง + ข้าวเหนียวดำเล็กน้อย",
                "ผัดไทยอกไก่เส้นบุก + ถั่วงอกและผักสด"
            ];

            const dinnerOptions = [
                "สลัดอกไก่ย่าง/ไข่ต้ม (น้ำสลัดงาญี่ปุ่นน้ำใส)",
                "ต้มยำกุ้งน้ำใส + ไข่เจียวไร้น้ำมัน (หม้อทอด) + ข้าวกล้อง",
                "ปลาย่างซอสเทอริยากิ + บรอกโคลีต้ม + ซุปมิโสะ",
                "แกงจืดเต้าหู้หมูสับใบตำลึง + ข้าวไรซ์เบอร์รี 1 ทัพพี",
                "ยำวูนเส้นอกไก่สับพริกสด + ผักแกล้มสด"
            ];

            const snackOptions = [
                "อัลมอนด์อบธรรมชาติ 10-15 เม็ด",
                "ฝรั่ง / แอปเปิลเขียว 1 ลูก",
                "เวย์โปรตีน 1 สกูป / นมโปรตีนสูง",
                "กล้วยหอม 1 ลูกก่อนออกกำลังกาย"
            ];

            const workoutOptions = [
                { title: goal === 'เพิ่มกล้ามเนื้อ' ? "Hypertrophy Chest & Triceps" : "Full Body HIIT & Cardio", detail: "Squats, Push-ups, Mountain Climbers ทำ 4 เซต เซตละ 45 วินาที", durationMinutes: 35 },
                { title: "Legs & Core Dynamic Workout", detail: "Lunges, Planks, Leg Raises 3-4 เซต เพื่อสร้างความแข็งแรงแกนกลางลำตัว", durationMinutes: 40 },
                { title: "Upper Body Strength & Toning", detail: "Dumbbell Press / Resistance Band Rows + Bicep Curls 4 เซต", durationMinutes: 45 },
                { title: "Active Recovery & Yoga Stretch", detail: "เดินเร็ว 30 นาที + ยืดเหยียดกล้ามเนื้อทั่วร่างกาย (Stretching)", durationMinutes: 30 }
            ];

            for (let i = 1; i <= days; i++) {
                const b = breakfastOptions[(i - 1) % breakfastOptions.length];
                const l = lunchOptions[(i - 1) % lunchOptions.length];
                const d = dinnerOptions[(i - 1) % dinnerOptions.length];
                const s = snackOptions[(i - 1) % snackOptions.length];
                const w = workoutOptions[(i - 1) % workoutOptions.length];

                plan.push({
                    day: i,
                    title: `วันที่ ${i}: ${goal === 'ลดน้ำหนัก' ? 'เน้นเผาผลาญไขมัน' : goal === 'เพิ่มกล้ามเนื้อ' ? 'เน้นสร้างกล้ามเนื้อ' : 'รักษาสมดุลโภชนาการ'}`,
                    estCalories: targetTdee,
                    meals: {
                        breakfast: b,
                        lunch: l,
                        dinner: d,
                        snack: s
                    },
                    workout: w,
                    completed: false
                });
            }

            return plan;
        }

        // Render Cards inside Container
        function renderPlanCards(data) {
            const container = document.getElementById('planContainer');
            const emptyState = document.getElementById('emptyState');
            container.innerHTML = '';

            if (!data || data.length === 0) {
                emptyState.classList.remove('hidden');
                return;
            }
            emptyState.classList.add('hidden');

            const searchTerm = document.getElementById('searchDay').value.toLowerCase();
            const filterValue = document.getElementById('filterDay').value;

            let filteredData = data.filter(item => {
                // Filter completion status
                if (filterValue === 'completed' && !item.completed) return false;
                if (filterValue === 'incomplete' && item.completed) return false;

                // Search term filter
                if (searchTerm) {
                    const matchTitle = item.title.toLowerCase().includes(searchTerm);
                    const matchBreakfast = item.meals.breakfast.toLowerCase().includes(searchTerm);
                    const matchLunch = item.meals.lunch.toLowerCase().includes(searchTerm);
                    const matchDinner = item.meals.dinner.toLowerCase().includes(searchTerm);
                    const matchWorkout = item.workout.title.toLowerCase().includes(searchTerm);
                    return matchTitle || matchBreakfast || matchLunch || matchDinner || matchWorkout;
                }
                return true;
            });

            if (filteredData.length === 0) {
                container.innerHTML = `
                    <div class="col-span-full text-center py-10 bg-white rounded-xl border border-stone-200 text-stone-500 text-xs">
                        ไม่พบแผนสุขภาพตรงตามคำค้นหาหรือตัวกรอง
                    </div>
                `;
                return;
            }

            filteredData.forEach(item => {
                const card = document.createElement('div');
                card.className = `bg-white rounded-2xl p-5 border ${item.completed ? 'border-emerald-300 bg-emerald-50/20' : 'border-stone-200/90'} shadow-sm hover:shadow-md transition duration-200 flex flex-col justify-between`;

                card.innerHTML = `
                    <div>
                        <!-- Header Row -->
                        <div class="flex items-center justify-between mb-3 pb-3 border-b border-stone-100">
                            <div class="flex items-center gap-2.5">
                                <label class="cursor-pointer flex items-center">
                                    <input type="checkbox" onchange="toggleDayComplete(${item.day})" ${item.completed ? 'checked' : ''} class="w-4 h-4 text-emerald-600 rounded border-stone-300 focus:ring-emerald-500 cursor-pointer">
                                </label>
                                <div>
                                    <span class="text-xs font-bold text-emerald-700 uppercase tracking-wider">Day ${item.day}</span>
                                    <h3 class="font-semibold text-stone-800 text-sm ${item.completed ? 'line-through text-stone-400' : ''}">${item.title}</h3>
                                </div>
                            </div>
                            <span class="text-[11px] font-medium bg-stone-100 text-stone-600 px-2 py-1 rounded-lg">
                                ~${item.estCalories || '--'} kcal
                            </span>
                        </div>

                        <!-- Meals Section -->
                        <div class="mb-4">
                            <h4 class="text-xs font-bold uppercase tracking-wide text-emerald-700 mb-2 flex items-center gap-1.5">
                                <i class="fa-solid fa-utensils"></i> เมนูอาหารประจำวัน
                            </h4>
                            <div class="space-y-1.5 text-xs">
                                <div class="bg-stone-50 p-2 rounded-xl border border-stone-100">
                                    <span class="font-semibold text-stone-700 block text-[11px] text-emerald-800">🍳 มื้อเช้า:</span>
                                    <p class="text-stone-600 mt-0.5">${item.meals.breakfast}</p>
                                </div>
                                <div class="bg-stone-50 p-2 rounded-xl border border-stone-100">
                                    <span class="font-semibold text-stone-700 block text-[11px] text-emerald-800">🥗 มื้อกลางวัน:</span>
                                    <p class="text-stone-600 mt-0.5">${item.meals.lunch}</p>
                                </div>
                                <div class="bg-stone-50 p-2 rounded-xl border border-stone-100">
                                    <span class="font-semibold text-stone-700 block text-[11px] text-emerald-800">🍲 มื้อเย็น:</span>
                                    <p class="text-stone-600 mt-0.5">${item.meals.dinner}</p>
                                </div>
                                ${item.meals.snack ? `
                                <div class="bg-amber-50/50 p-2 rounded-xl border border-amber-100/60">
                                    <span class="font-semibold text-amber-800 block text-[11px]">🍎 อาหารว่าง / ของว่าง:</span>
                                    <p class="text-stone-600 mt-0.5">${item.meals.snack}</p>
                                </div>
                                ` : ''}
                            </div>
                        </div>

                        <!-- Workout Section -->
                        <div>
                            <h4 class="text-xs font-bold uppercase tracking-wide text-stone-700 mb-2 flex items-center justify-between">
                                <span class="flex items-center gap-1.5">
                                    <i class="fa-solid fa-person-running text-stone-800"></i> โปรแกรมออกกำลังกาย
                                </span>
                                ${item.workout.durationMinutes ? `<span class="text-[10px] text-stone-400 font-normal"><i class="fa-regular fa-clock"></i> ${item.workout.durationMinutes} นาที</span>` : ''}
                            </h4>
                            <div class="bg-stone-50 p-3 rounded-xl border border-stone-100 text-xs">
                                <strong class="text-stone-800 block mb-1 font-medium">${item.workout.title}</strong>
                                <p class="text-stone-600 text-[11px] leading-relaxed">${item.workout.detail}</p>
                            </div>
                        </div>
                    </div>

                    <!-- Footer Check Box action inside card -->
                    <div class="mt-4 pt-2 border-t border-stone-100 flex items-center justify-between text-xs text-stone-400">
                        <span>สถานะกิจกรรม</span>
                        <button onclick="toggleDayComplete(${item.day})" class="text-xs font-medium text-emerald-600 hover:text-emerald-800">
                            ${item.completed ? '<i class="fa-solid fa-circle-check text-emerald-600"></i> ทำเสร็จแล้ว' : '<i class="fa-regular fa-circle"></i> ทำเครื่องหมายว่าเสร็จ'}
                        </button>
                    </div>
                `;
                container.appendChild(card);
            });

            updateProgressTracker();
        }

        // Toggle Day Completion
        function toggleDayComplete(dayNum) {
            const target = currentPlanData.find(d => d.day === dayNum);
            if (target) {
                target.completed = !target.completed;
                renderPlanCards(currentPlanData);
            }
        }

        // Update top progress bar
        function updateProgressTracker() {
            if (!currentPlanData || currentPlanData.length === 0) return;
            const completedCount = currentPlanData.filter(d => d.completed).length;
            const percentage = Math.round((completedCount / currentPlanData.length) * 100);

            document.getElementById('progressBar').style.width = `${percentage}%`;
            document.getElementById('progressPercent').textContent = `${percentage}% (${completedCount}/${currentPlanData.length} วัน)`;
        }

        // Form Submit Handler
        document.getElementById('healthForm').addEventListener('submit', async (e) => {
            e.preventDefault();

            const gender = document.getElementById('gender').value;
            const weight = parseFloat(document.getElementById('weight').value);
            const height = parseFloat(document.getElementById('height').value);
            const age = parseInt(document.getElementById('age').value) || 28;
            const goal = document.getElementById('goal').value;
            const days = parseInt(document.getElementById('days').value) || 7;
            const activity = document.getElementById('activity').value;

            // Collect selected dietary preferences
            const dietPrefs = Array.from(document.querySelectorAll('.diet-pref:checked')).map(cb => cb.value);

            // 1. Calculate BMI
            const bmiInfo = calculateBMI(weight, height, gender);
            const energyInfo = calculateEnergy(gender, weight, height, age, activity, goal);

            // 2. Render Results Banner
            const bmiBanner = document.getElementById('bmiResult');
            document.getElementById('bmiValue').textContent = bmiInfo.bmi;
            document.getElementById('bmiStatusText').textContent = bmiInfo.status;
            document.getElementById('bmrValue').textContent = energyInfo.bmr;
            document.getElementById('tdeeValue').textContent = energyInfo.tdee;

            bmiBanner.className = `mt-6 p-5 rounded-2xl border transition-all ${bmiInfo.colorClass}`;
            bmiBanner.classList.remove('hidden');

            // 3. UI Loading state
            document.getElementById('loading').classList.remove('hidden');
            document.getElementById('planContainer').innerHTML = '';
            document.getElementById('planToolbar').classList.add('hidden');
            document.getElementById('emptyState').classList.add('hidden');

            // 4. Fetch AI Plan
            const rawPlan = await fetchPlanFromGeminiAPI(gender, weight, height, age, goal, days, bmiInfo.bmi, bmiInfo.status, energyInfo.tdee, dietPrefs);

            // Format raw data with completion state
            currentPlanData = rawPlan.map(item => ({
                ...item,
                completed: false
            }));

            // Hide loading & Render
            document.getElementById('loading').classList.add('hidden');
            document.getElementById('planToolbar').classList.remove('hidden');
            renderPlanCards(currentPlanData);
        });

        // Filter & Search Event Listeners
        document.getElementById('searchDay').addEventListener('input', () => renderPlanCards(currentPlanData));
        document.getElementById('filterDay').addEventListener('change', () => renderPlanCards(currentPlanData));

        // Reset App State
        document.getElementById('resetAppBtn').addEventListener('click', () => {
            currentPlanData = [];
            document.getElementById('healthForm').reset();
            document.getElementById('bmiResult').classList.add('hidden');
            document.getElementById('planToolbar').classList.add('hidden');
            document.getElementById('planContainer').innerHTML = '';
            document.getElementById('emptyState').classList.remove('hidden');
        });
    </script>
</body>
</html>
