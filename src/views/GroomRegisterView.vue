<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-3xl mx-auto">
      <div class="card mb-8">
        <h1 class="text-3xl font-bold text-primary-700 mb-6">تسجيل عريس</h1>
        
        <form @submit.prevent="submitForm">
          <div class="mb-8">
            <h2 class="text-xl font-semibold text-gray-700 mb-4">المعلومات الشخصية</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="form-group">
                <label for="fullName" class="label">الاسم الكامل</label>
                <input 
                  id="fullName"
                  v-model="formData.fullName"
                  type="text"
                  class="input-field"
                  required
                />
              </div>
              
              <div class="form-group">
                <label for="age" class="label">العمر</label>
                <input 
                  id="age"
                  v-model="formData.age"
                  type="number"
                  min="18"
                  max="70"
                  class="input-field"
                  required
                />
              </div>
              
              <div class="form-group">
                <label for="height" class="label">الطول (سم)</label>
                <input 
                  id="height"
                  v-model="formData.height"
                  type="number"
                  class="input-field"
                  required
                />
              </div>
              
              <div class="form-group">
                <label for="profession" class="label">المهنة</label>
                <input 
                  id="profession"
                  v-model="formData.profession"
                  type="text"
                  class="input-field"
                  required
                />
              </div>
              
              <div class="form-group">
                <label for="education" class="label">المستوى التعليمي</label>
                <select 
                  id="education"
                  v-model="formData.education"
                  class="input-field"
                  required
                >
                  <option value="">اختر المستوى التعليمي</option>
                  <option value="high_school">ثانوية عامة</option>
                  <option value="diploma">دبلوم</option>
                  <option value="bachelors">بكالوريوس</option>
                  <option value="masters">ماجستير</option>
                  <option value="phd">دكتوراه</option>
                </select>
              </div>
              
              <div class="form-group">
                <label for="income" class="label">الدخل الشهري</label>
                <select 
                  id="income"
                  v-model="formData.income"
                  class="input-field"
                  required
                >
                  <option value="">اختر مستوى الدخل</option>
                  <option value="low">أقل من 5,000</option>
                  <option value="medium">5,000 - 10,000</option>
                  <option value="high">10,000 - 20,000</option>
                  <option value="very_high">أكثر من 20,000</option>
                </select>
              </div>
              
              <div class="form-group md:col-span-2">
                <label for="location" class="label">مكان الإقامة</label>
                <input 
                  id="location"
                  v-model="formData.location"
                  type="text"
                  class="input-field"
                  required
                />
              </div>
              
              <div class="form-group md:col-span-2">
                <label for="religiousCommitment" class="label">الالتزام الديني</label>
                <select 
                  id="religiousCommitment"
                  v-model="formData.religiousCommitment"
                  class="input-field"
                  required
                >
                  <option value="">اختر مستوى الالتزام</option>
                  <option value="low">ملتزم ببعض الواجبات</option>
                  <option value="medium">ملتزم بمعظم الواجبات</option>
                  <option value="high">ملتزم بالكامل</option>
                </select>
              </div>
              
              <div class="form-group md:col-span-2">
                <label for="bio" class="label">نبذة شخصية</label>
                <textarea 
                  id="bio"
                  v-model="formData.bio"
                  rows="4"
                  class="input-field"
                  required
                ></textarea>
              </div>
            </div>
          </div>
          
          <div class="mb-8">
            <h2 class="text-xl font-semibold text-gray-700 mb-4">معلومات الاتصال</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
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
              
              <div class="form-group">
                <label for="phone" class="label">رقم الهاتف</label>
                <input 
                  id="phone"
                  v-model="formData.phone"
                  type="tel"
                  class="input-field"
                  required
                />
              </div>
            </div>
          </div>
          
          <div class="mb-8">
            <h2 class="text-xl font-semibold text-gray-700 mb-4">مواصفات الزوجة المطلوبة</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="form-group">
                <label for="preferredAgeMin" class="label">العمر (من)</label>
                <input 
                  id="preferredAgeMin"
                  v-model="formData.preferredTraits.ageMin"
                  type="number"
                  min="18"
                  max="60"
                  class="input-field"
                  required
                />
              </div>
              
              <div class="form-group">
                <label for="preferredAgeMax" class="label">العمر (إلى)</label>
                <input 
                  id="preferredAgeMax"
                  v-model="formData.preferredTraits.ageMax"
                  type="number"
                  min="18"
                  max="60"
                  class="input-field"
                  required
                />
              </div>
              
              <div class="form-group">
                <label for="preferredEducation" class="label">المستوى التعليمي</label>
                <select 
                  id="preferredEducation"
                  v-model="formData.preferredTraits.education"
                  class="input-field"
                  required
                >
                  <option value="">اختر المستوى التعليمي</option>
                  <option value="any">غير مهم</option>
                  <option value="high_school">ثانوية عامة</option>
                  <option value="diploma">دبلوم</option>
                  <option value="bachelors">بكالوريوس</option>
                  <option value="higher">دراسات عليا</option>
                </select>
              </div>
              
              <div class="form-group md:col-span-2">
                <label for="preferredReligiousCommitment" class="label">مستوى الالتزام الديني</label>
                <select 
                  id="preferredReligiousCommitment"
                  v-model="formData.preferredTraits.religiousCommitment"
                  class="input-field"
                  required
                >
                  <option value="">اختر مستوى الالتزام</option>
                  <option value="any">غير مهم</option>
                  <option value="low">ملتزمة ببعض الواجبات</option>
                  <option value="medium">ملتزمة بمعظم الواجبات</option>
                  <option value="high">ملتزمة بالكامل</option>
                </select>
              </div>
              
              <div class="form-group md:col-span-2">
                <label for="otherPreferences" class="label">مواصفات أخرى</label>
                <textarea 
                  id="otherPreferences"
                  v-model="formData.preferredTraits.otherPreferences"
                  rows="3"
                  class="input-field"
                ></textarea>
              </div>
            </div>
          </div>
          
          <div class="form-group">
            <div class="flex items-start mb-4">
              <div class="flex items-center h-5">
                <input 
                  id="terms" 
                  type="checkbox" 
                  v-model="formData.termsAccepted"
                  class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300"
                  required
                />
              </div>
              <label for="terms" class="mr-2 text-sm font-medium text-gray-700">
                أوافق على <router-link to="/terms" class="text-primary-600 hover:underline">الشروط والأحكام</router-link> وأقر بصحة المعلومات المقدمة
              </label>
            </div>
          </div>
          
          <div class="flex justify-end">
            <button 
              type="button" 
              @click="resetForm" 
              class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-bold py-2 px-4 rounded ml-2"
            >
              إعادة تعيين
            </button>
            <button 
              type="submit" 
              class="btn-primary"
              :disabled="!formData.termsAccepted"
              :class="{ 'opacity-50 cursor-not-allowed': !formData.termsAccepted }"
            >
              إرسال
            </button>
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

const formData = ref({
  fullName: '',
  age: null,
  height: null,
  profession: '',
  education: '',
  income: '',
  location: '',
  religiousCommitment: '',
  bio: '',
  email: '',
  phone: '',
  termsAccepted: false,
  preferredTraits: {
    ageMin: 18,
    ageMax: 35,
    education: '',
    religiousCommitment: '',
    otherPreferences: ''
  }
})

const submitForm = () => {
  // Here you would typically send the form data to your backend
  console.log('Form submitted:', formData.value)
  
  // For now, we'll just simulate a successful submission and navigate to confirmation
  alert('تم تسجيل بياناتك بنجاح. سيتم مراجعتها من قبل فريق المنصة.')
  router.push('/')
}

const resetForm = () => {
  formData.value = {
    fullName: '',
    age: null,
    height: null,
    profession: '',
    education: '',
    income: '',
    location: '',
    religiousCommitment: '',
    bio: '',
    email: '',
    phone: '',
    termsAccepted: false,
    preferredTraits: {
      ageMin: 18,
      ageMax: 35,
      education: '',
      religiousCommitment: '',
      otherPreferences: ''
    }
  }
}
</script> 