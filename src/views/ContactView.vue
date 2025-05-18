<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-3xl mx-auto">
      <div class="card mb-8">
        <h1 class="text-3xl font-bold text-primary-700 mb-6">اتصل بنا</h1>
        
        <p class="text-gray-600 mb-6">
          يسعدنا تواصلك معنا. يرجى ملء النموذج أدناه وسنرد على استفسارك في أقرب وقت ممكن.
        </p>
        
        <form @submit.prevent="submitForm">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
            <div class="form-group">
              <label for="name" class="label">الاسم الكامل</label>
              <input 
                id="name"
                v-model="formData.name"
                type="text"
                class="input-field"
                required
              />
            </div>
            
            <div class="form-group">
              <label for="email" class="label">البريد الإلكتروني</label>
              <input 
                id="email"
                v-model="formData.email"
                type="email"
                class="input-field"
                required
              />
            </div>
            
            <div class="form-group md:col-span-2">
              <label for="subject" class="label">الموضوع</label>
              <input 
                id="subject"
                v-model="formData.subject"
                type="text"
                class="input-field"
                required
              />
            </div>
            
            <div class="form-group md:col-span-2">
              <label for="message" class="label">الرسالة</label>
              <textarea 
                id="message"
                v-model="formData.message"
                rows="6"
                class="input-field"
                required
              ></textarea>
            </div>
          </div>
          
          <div class="flex justify-end">
            <button 
              type="submit" 
              class="btn-primary"
            >
              إرسال
            </button>
          </div>
        </form>
        
        <div class="mt-12 pt-8 border-t border-gray-200">
          <h2 class="text-xl font-semibold text-gray-700 mb-4">معلومات الاتصال</h2>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex items-start">
              <div class="bg-primary-100 rounded-full p-3 ml-4 text-primary-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-gray-800 mb-1">البريد الإلكتروني</h3>
                <p class="text-gray-600">info@zawgny.com</p>
              </div>
            </div>
            
            <div class="flex items-start">
              <div class="bg-primary-100 rounded-full p-3 ml-4 text-primary-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-gray-800 mb-1">رقم الهاتف</h3>
                <p class="text-gray-600">+966 12 345 6789</p>
              </div>
            </div>
            
            <div class="flex items-start">
              <div class="bg-primary-100 rounded-full p-3 ml-4 text-primary-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-gray-800 mb-1">العنوان</h3>
                <p class="text-gray-600">شارع الملك فهد، الرياض، المملكة العربية السعودية</p>
              </div>
            </div>
            
            <div class="flex items-start">
              <div class="bg-primary-100 rounded-full p-3 ml-4 text-primary-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-gray-800 mb-1">ساعات العمل</h3>
                <p class="text-gray-600">الأحد - الخميس: 9 صباحاً - 5 مساءً</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const formData = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const submitForm = () => {
  // Here you would typically send the form data to your backend
  console.log('Form submitted:', formData.value)
  
  // For now, we'll just simulate a successful submission and show an alert
  alert('تم إرسال رسالتك بنجاح. سنتواصل معك في أقرب وقت ممكن.')
  
  // Reset the form
  formData.value = {
    name: '',
    email: '',
    subject: '',
    message: ''
  }
}
</script> 