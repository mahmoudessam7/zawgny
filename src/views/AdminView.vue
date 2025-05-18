<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-6xl mx-auto">
      <div class="card mb-8">
        <h1 class="text-3xl font-bold text-gray-800 mb-6">لوحة تحكم المدير</h1>
        
        <!-- Statistics Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div class="bg-primary-50 p-6 rounded-lg shadow-sm">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-primary-600 font-medium">العرسان</p>
                <h3 class="text-3xl font-bold text-primary-800">{{ groomCount }}</h3>
              </div>
              <div class="bg-primary-200 rounded-full p-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
              </div>
            </div>
            <div class="mt-4">
              <a href="#grooms-section" class="text-sm text-primary-600 hover:text-primary-800">عرض التفاصيل →</a>
            </div>
          </div>
          
          <div class="bg-secondary-50 p-6 rounded-lg shadow-sm">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-secondary-600 font-medium">العرائس</p>
                <h3 class="text-3xl font-bold text-secondary-800">{{ brideCount }}</h3>
              </div>
              <div class="bg-secondary-200 rounded-full p-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-secondary-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
              </div>
            </div>
            <div class="mt-4">
              <a href="#brides-section" class="text-sm text-secondary-600 hover:text-secondary-800">عرض التفاصيل →</a>
            </div>
          </div>
          
          <div class="bg-green-50 p-6 rounded-lg shadow-sm">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-green-600 font-medium">عمليات الزواج الناجحة</p>
                <h3 class="text-3xl font-bold text-green-800">{{ matchCount }}</h3>
              </div>
              <div class="bg-green-200 rounded-full p-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
              </div>
            </div>
            <div class="mt-4">
              <a href="#matches-section" class="text-sm text-green-600 hover:text-green-800">عرض التفاصيل →</a>
            </div>
          </div>
        </div>
        
        <!-- Grooms Table -->
        <div id="grooms-section" class="mb-12">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold text-gray-700">قائمة العرسان</h2>
            <div class="flex space-x-4">
              <input 
                type="text" 
                v-model="groomSearch" 
                placeholder="بحث..." 
                class="px-3 py-2 border border-gray-300 rounded-md"
              />
              <button @click="filterGrooms" class="btn-primary">بحث</button>
            </div>
          </div>
          
          <div class="overflow-x-auto bg-white rounded-lg shadow">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">الاسم</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">العمر</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">المهنة</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">المستوى التعليمي</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">الإجراءات</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="groom in grooms" :key="groom.id">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ groom.fullName }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ groom.age }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ groom.profession }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ getEducationLabel(groom.education) }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                    <button @click="viewProfile(groom)" class="text-primary-600 hover:text-primary-900 ml-4">عرض الملف</button>
                    <button @click="matchWith(groom)" class="text-green-600 hover:text-green-900">مطابقة مع</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        
        <!-- Brides Table -->
        <div id="brides-section" class="mb-12">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold text-gray-700">قائمة العرائس</h2>
            <div class="flex space-x-4">
              <input 
                type="text" 
                v-model="brideSearch" 
                placeholder="بحث..." 
                class="px-3 py-2 border border-gray-300 rounded-md"
              />
              <button @click="filterBrides" class="btn-secondary">بحث</button>
            </div>
          </div>
          
          <div class="overflow-x-auto bg-white rounded-lg shadow">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">الاسم</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">العمر</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">المهنة</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">المستوى التعليمي</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">الإجراءات</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="bride in brides" :key="bride.id">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ bride.fullName }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ bride.age }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ bride.profession }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ getEducationLabel(bride.education) }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                    <button @click="viewProfile(bride)" class="text-primary-600 hover:text-primary-900 ml-4">عرض الملف</button>
                    <button @click="matchWith(bride)" class="text-green-600 hover:text-green-900">مطابقة مع</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        
        <!-- Recent Matches -->
        <div id="matches-section">
          <h2 class="text-xl font-semibold text-gray-700 mb-4">المطابقات الأخيرة</h2>
          <div class="overflow-x-auto bg-white rounded-lg shadow">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">العريس</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">العروس</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">تاريخ المطابقة</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">الحالة</th>
                  <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">الإجراءات</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="match in matches" :key="match.id">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ match.groom.fullName }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ match.bride.fullName }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatDate(match.matchDate) }}</td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span :class="{
                      'px-2 py-1 text-xs rounded-full': true,
                      'bg-yellow-100 text-yellow-800': match.status === 'pending',
                      'bg-green-100 text-green-800': match.status === 'success',
                      'bg-red-100 text-red-800': match.status === 'failed'
                    }">
                      {{ getStatusLabel(match.status) }}
                    </span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                    <button @click="viewMatch(match)" class="text-primary-600 hover:text-primary-900 ml-4">عرض التفاصيل</button>
                    <button 
                      v-if="match.status === 'pending'"
                      @click="updateMatchStatus(match.id, 'success')" 
                      class="text-green-600 hover:text-green-900"
                    >
                      تأكيد
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Mock data for demonstration
const groomCount = ref(15)
const brideCount = ref(12)
const matchCount = ref(5)

const groomSearch = ref('')
const brideSearch = ref('')

// Sample grooms data
const grooms = ref([
  { id: 1, fullName: 'محمد أحمد', age: 32, profession: 'مهندس', education: 'bachelors' },
  { id: 2, fullName: 'أحمد محمود', age: 28, profession: 'طبيب', education: 'masters' },
  { id: 3, fullName: 'خالد عبدالله', age: 35, profession: 'محاسب', education: 'bachelors' },
  { id: 4, fullName: 'عمر فاروق', age: 30, profession: 'مدرس', education: 'phd' }
])

// Sample brides data
const brides = ref([
  { id: 1, fullName: 'فاطمة علي', age: 27, profession: 'مهندسة', education: 'bachelors' },
  { id: 2, fullName: 'سارة محمد', age: 25, profession: 'طبيبة', education: 'masters' },
  { id: 3, fullName: 'نورا أحمد', age: 30, profession: 'محاسبة', education: 'bachelors' },
  { id: 4, fullName: 'مريم خالد', age: 26, profession: 'مدرسة', education: 'bachelors' }
])

// Sample matches data
const matches = ref([
  { 
    id: 1, 
    groom: { id: 1, fullName: 'محمد أحمد' }, 
    bride: { id: 2, fullName: 'سارة محمد' },
    matchDate: new Date(2023, 4, 15),
    status: 'success'
  },
  { 
    id: 2, 
    groom: { id: 3, fullName: 'خالد عبدالله' }, 
    bride: { id: 1, fullName: 'فاطمة علي' },
    matchDate: new Date(2023, 5, 10),
    status: 'pending'
  },
  { 
    id: 3, 
    groom: { id: 2, fullName: 'أحمد محمود' }, 
    bride: { id: 4, fullName: 'مريم خالد' },
    matchDate: new Date(2023, 3, 22),
    status: 'failed'
  }
])

// Function to convert education codes to readable labels
const getEducationLabel = (code) => {
  const educationMap = {
    'high_school': 'ثانوية عامة',
    'diploma': 'دبلوم',
    'bachelors': 'بكالوريوس',
    'masters': 'ماجستير',
    'phd': 'دكتوراه'
  }
  
  return educationMap[code] || code
}

// Function to format dates
const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ar-SA')
}

// Function to get status label
const getStatusLabel = (status) => {
  const statusMap = {
    'pending': 'قيد الانتظار',
    'success': 'تمت بنجاح',
    'failed': 'لم تتم'
  }
  
  return statusMap[status] || status
}

// Function to filter grooms
const filterGrooms = () => {
  // This would typically involve an API call or filtering local data
  console.log('Filtering grooms with:', groomSearch.value)
  // Here we're just simulating the functionality
}

// Function to filter brides
const filterBrides = () => {
  // This would typically involve an API call or filtering local data
  console.log('Filtering brides with:', brideSearch.value)
  // Here we're just simulating the functionality
}

// Function to view profile details
const viewProfile = (person) => {
  // In a real application, this would navigate to a detailed profile page
  console.log('Viewing profile:', person)
  alert(`عرض الملف الشخصي لـ ${person.fullName}`)
}

// Function to match people
const matchWith = (person) => {
  // In a real application, this would open a matching interface
  console.log('Matching with:', person)
  alert(`تم فتح واجهة المطابقة لـ ${person.fullName}`)
}

// Function to view match details
const viewMatch = (match) => {
  // In a real application, this would navigate to match details
  console.log('Viewing match:', match)
  alert(`عرض تفاصيل المطابقة بين ${match.groom.fullName} و ${match.bride.fullName}`)
}

// Function to update match status
const updateMatchStatus = (matchId, newStatus) => {
  // In a real application, this would update the status via an API
  console.log('Updating match status:', matchId, newStatus)
  
  // Here we're just updating the local data
  const matchIndex = matches.value.findIndex(m => m.id === matchId)
  if (matchIndex !== -1) {
    matches.value[matchIndex].status = newStatus
    
    if (newStatus === 'success') {
      matchCount.value++
      alert('تم تأكيد المطابقة بنجاح')
    }
  }
}
</script> 