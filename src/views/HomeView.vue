<template>
  <main>
    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-primary-50 to-primary-100 py-20 relative overflow-hidden">
      <div class="absolute inset-0 opacity-10 bg-heart-pattern bg-repeat"></div>
      <div class="container mx-auto px-4 relative z-10">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-5xl md:text-6xl font-bold text-primary-800 mb-6 font-arabic">زوجني</h1>
          <p class="text-2xl text-primary-700 mb-8 font-arabic">
            المنصة المثالية للزواج الشرعي وفق تعاليم الإسلام
          </p>
          <div class="flex flex-col sm:flex-row gap-6 justify-center">
            <router-link to="/groom-register" class="bg-primary-600 hover:bg-primary-700 text-white font-bold py-3 px-8 rounded-lg text-center transition-colors shadow-md">
              تسجيل كعريس
            </router-link>
            <router-link to="/bride-register" class="bg-secondary-500 hover:bg-secondary-600 text-white font-bold py-3 px-8 rounded-lg text-center transition-colors shadow-md">
              تسجيل كعروس
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="py-20 bg-white">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl font-bold text-primary-800 mb-8 text-center">كيف تعمل المنصة؟</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10 max-w-5xl mx-auto">
          <div class="bg-white shadow-lg rounded-lg p-8 text-center border border-secondary-100">
            <div class="rounded-full w-20 h-20 bg-primary-100 flex items-center justify-center mx-auto mb-6 text-primary-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-primary-700 mb-4">التسجيل</h3>
            <p class="text-gray-600 text-lg">
              سجل بياناتك ومواصفات شريك حياتك المستقبلي بكل سرية وخصوصية
            </p>
          </div>

          <div class="bg-white shadow-lg rounded-lg p-8 text-center border border-secondary-100">
            <div class="rounded-full w-20 h-20 bg-primary-100 flex items-center justify-center mx-auto mb-6 text-primary-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-primary-700 mb-4">المطابقة</h3>
            <p class="text-gray-600 text-lg">
              يقوم المشرفون المتخصصون بمراجعة البيانات وإيجاد التوافق المناسب
            </p>
          </div>

          <div class="bg-white shadow-lg rounded-lg p-8 text-center border border-secondary-100">
            <div class="rounded-full w-20 h-20 bg-primary-100 flex items-center justify-center mx-auto mb-6 text-primary-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-primary-700 mb-4">التعارف</h3>
            <p class="text-gray-600 text-lg">
              عند وجود توافق، يتم التواصل بين الطرفين تحت إشراف المنصة
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 bg-secondary-50 relative">
      <div class="absolute inset-0 opacity-5 bg-wedding-texture bg-repeat"></div>
      <div class="container mx-auto px-4 relative z-10">
        <h2 class="text-3xl font-bold text-primary-800 mb-10 text-center">مميزات المنصة</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-10 max-w-5xl mx-auto">
          <div class="bg-white shadow-lg rounded-lg p-8 flex items-start border-t-4 border-primary-500">
            <div class="bg-primary-100 rounded-full p-4 ml-5 text-primary-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-bold text-primary-700 mb-3">خصوصية وأمان</h3>
              <p class="text-gray-600 text-lg">
                نحافظ على خصوصية بياناتك ولا يمكن الإطلاع عليها إلا من قبل المشرفين المختصين
              </p>
            </div>
          </div>

          <div class="bg-white shadow-lg rounded-lg p-8 flex items-start border-t-4 border-primary-500">
            <div class="bg-primary-100 rounded-full p-4 ml-5 text-primary-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-bold text-primary-700 mb-3">توافق شرعي</h3>
              <p class="text-gray-600 text-lg">
                جميع مراحل التعارف تتم وفق الضوابط الشرعية بإشراف متخصصين
              </p>
            </div>
          </div>

          <div class="bg-white shadow-lg rounded-lg p-8 flex items-start border-t-4 border-primary-500">
            <div class="bg-primary-100 rounded-full p-4 ml-5 text-primary-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-bold text-primary-700 mb-3">استشارات متخصصة</h3>
              <p class="text-gray-600 text-lg">
                نقدم استشارات أسرية وزوجية متخصصة تساعد على اختيار الشريك المناسب
              </p>
            </div>
          </div>

          <div class="bg-white shadow-lg rounded-lg p-8 flex items-start border-t-4 border-primary-500">
            <div class="bg-primary-100 rounded-full p-4 ml-5 text-primary-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-bold text-primary-700 mb-3">بيانات موثقة</h3>
              <p class="text-gray-600 text-lg">
                نتحقق من جميع البيانات المقدمة للتأكد من صحتها قبل إجراء أي مطابقة
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="py-20 bg-white">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl font-bold text-primary-800 mb-10 text-center">قصص نجاح</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
          <div class="bg-white shadow-lg rounded-lg p-8 border border-secondary-200 relative">
            <div class="absolute -top-4 right-8 text-5xl text-primary-300 leading-none">"</div>
            <div class="flex items-center mb-6">
              <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center text-primary-600 font-bold text-2xl ml-4">
                أ
              </div>
              <div>
                <h3 class="font-bold text-xl text-primary-800">أحمد ونورة</h3>
                <p class="text-primary-500 text-md">تم الزواج منذ 6 أشهر</p>
              </div>
            </div>
            <p class="text-gray-600 text-lg relative z-10">
              "الحمد لله، وجدت شريكة حياتي عن طريق منصة زوجني. كان التوافق كبيرًا في القيم والأهداف، ونشكر القائمين على هذه المنصة المباركة."
            </p>
          </div>

          <div class="bg-white shadow-lg rounded-lg p-8 border border-secondary-200 relative">
            <div class="absolute -top-4 right-8 text-5xl text-primary-300">"</div>
            <div class="flex items-center mb-6">
              <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center text-primary-600 font-bold text-2xl ml-4">
                س
              </div>
              <div>
                <h3 class="font-bold text-xl text-primary-800">سارة ومحمد</h3>
                <p class="text-primary-500 text-md">تم الزواج منذ سنة</p>
              </div>
            </div>
            <p class="text-gray-600 text-lg relative z-10">
              "كنت قلقة من التسجيل في البداية، لكن وجدت خصوصية عالية واهتمام من المشرفين. الحمد لله تم نصيبي مع زوجي الذي يشاركني نفس الأفكار والطموحات."
            </p>
          </div>

          <div class="bg-white shadow-lg rounded-lg p-8 border border-secondary-200 relative md:hidden lg:block">
            <div class="absolute -top-4 right-8 text-5xl text-primary-300">"</div>
            <div class="flex items-center mb-6">
              <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center text-primary-600 font-bold text-2xl ml-4">
                ع
              </div>
              <div>
                <h3 class="font-bold text-xl text-primary-800">عبدالله وعائشة</h3>
                <p class="text-primary-500 text-md">تم الزواج منذ 3 أشهر</p>
              </div>
            </div>
            <p class="text-gray-600 text-lg relative z-10">
              "منصة زوجني كانت السبب بعد الله في زواجي. لم أكن أتوقع أن أجد التوافق بهذه السرعة، لكن إجراءات المنصة المنظمة وفريق العمل المحترف سهّل الأمر كثيرًا."
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-br from-primary-600 to-primary-700 text-white relative overflow-hidden">
      <div class="absolute inset-0 opacity-10 bg-heart-pattern bg-repeat"></div>
      <div class="container mx-auto px-4 text-center relative z-10">
        <h2 class="text-4xl font-bold mb-8">ابدأ رحلتك نحو الزواج الناجح</h2>
        <p class="text-2xl mb-10 max-w-3xl mx-auto">
          سجل الآن وكن أحد المستفيدين من خدماتنا المتميزة في إيجاد شريك الحياة المناسب
        </p>
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <router-link to="/groom-register" class="bg-white text-primary-700 hover:bg-gray-100 font-bold py-4 px-10 rounded-lg transition-colors shadow-lg text-xl">
            تسجيل كعريس
          </router-link>
          <router-link to="/bride-register" class="bg-transparent border-2 border-white text-white hover:bg-white hover:text-primary-700 font-bold py-4 px-10 rounded-lg transition-colors shadow-lg text-xl">
            تسجيل كعروس
          </router-link>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
// No imports needed
</script>
