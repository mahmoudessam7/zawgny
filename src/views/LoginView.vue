<template>
  <div class="container mx-auto px-4 py-16">
    <div class="max-w-md mx-auto">
      <div class="card">
        <h1 class="text-2xl font-bold text-gray-800 mb-6 text-center">تسجيل الدخول</h1>
        
        <form @submit.prevent="login">
          <div class="form-group">
            <label for="email" class="label">البريد الإلكتروني</label>
            <input 
              id="email"
              v-model="email"
              type="email"
              class="input-field"
              required
            />
          </div>
          
          <div class="form-group">
            <label for="password" class="label">كلمة المرور</label>
            <input 
              id="password"
              v-model="password"
              type="password"
              class="input-field"
              required
            />
          </div>
          
          <div class="flex justify-between items-center mt-6">
            <div class="flex items-center">
              <input 
                id="remember" 
                type="checkbox" 
                v-model="remember"
                class="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded" 
              />
              <label for="remember" class="mr-2 block text-sm text-gray-700">تذكرني</label>
            </div>
            
            <a href="#" class="text-sm text-primary-600 hover:text-primary-500">نسيت كلمة المرور؟</a>
          </div>
          
          <div class="mt-6">
            <button 
              type="submit" 
              class="btn-primary w-full"
              :class="{ 'opacity-75': isLoading }"
              :disabled="isLoading"
            >
              <span v-if="isLoading">جاري التحميل...</span>
              <span v-else>تسجيل الدخول</span>
            </button>
          </div>
          
          <div v-if="error" class="mt-4 p-3 bg-red-50 text-red-700 rounded text-center">
            {{ error }}
          </div>

          <div class="mt-4 text-center text-gray-500 text-sm">
            <p>لتسجيل الدخول للاختبار استخدم:</p>
            <p>البريد الإلكتروني: admin@example.com</p>
            <p>كلمة المرور: admin123</p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const password = ref('')
const remember = ref(false)
const error = ref('')
const isLoading = ref(false)

const login = async () => {
  error.value = ''
  isLoading.value = true
  
  try {
    // This is a simplified login - in a real app, you would verify credentials with a backend
    await new Promise(resolve => setTimeout(resolve, 1000)) // Simulate API delay
    
    if (email.value === 'admin@example.com' && password.value === 'admin123') {
      // Store admin status - in a real app, you would use proper token-based authentication
      localStorage.setItem('isAdmin', 'true')
      router.push('/admin')
    } else {
      error.value = 'البريد الإلكتروني أو كلمة المرور غير صحيحة'
    }
  } catch (err) {
    error.value = 'حدث خطأ أثناء تسجيل الدخول'
    console.error(err)
  } finally {
    isLoading.value = false
  }
}
</script> 