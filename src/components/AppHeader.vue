<template>
  <header class="bg-white shadow-sm sticky top-0 z-50">
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center py-4">
        <div class="flex items-center">
          <router-link to="/" class="text-2xl font-bold text-primary-700">
            زوجني
          </router-link>
        </div>
        
        <nav class="hidden md:flex">
          <router-link 
            to="/" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
          >
            الرئيسية
          </router-link>
          
          <router-link 
            to="/groom-register" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
          >
            تسجيل عريس
          </router-link>
          
          <router-link 
            to="/bride-register" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
          >
            تسجيل عروس
          </router-link>
          
          <router-link 
            to="/about" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
          >
            عن المنصة
          </router-link>
          
          <router-link 
            to="/contact" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
          >
            اتصل بنا
          </router-link>
        </nav>
        
        <div class="flex items-center space-x-4">
          <router-link 
            to="/login" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium hidden md:block"
          >
            تسجيل الدخول
          </router-link>
          
          <button 
            @click="toggleMobileMenu" 
            type="button" 
            class="md:hidden p-2 rounded-md text-gray-700 hover:text-primary-600 focus:outline-none"
          >
            <svg 
              class="h-6 w-6" 
              fill="none" 
              viewBox="0 0 24 24" 
              stroke="currentColor"
            >
              <path 
                v-if="!mobileMenuOpen" 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M4 6h16M4 12h16M4 18h16"
              />
              <path 
                v-else 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>
      
      <!-- Mobile menu -->
      <div 
        v-if="mobileMenuOpen" 
        class="md:hidden pb-4"
      >
        <div class="flex flex-col space-y-2">
          <router-link 
            to="/" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
            @click="mobileMenuOpen = false"
          >
            الرئيسية
          </router-link>
          
          <router-link 
            to="/groom-register" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
            @click="mobileMenuOpen = false"
          >
            تسجيل عريس
          </router-link>
          
          <router-link 
            to="/bride-register" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
            @click="mobileMenuOpen = false"
          >
            تسجيل عروس
          </router-link>
          
          <router-link 
            to="/about" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
            @click="mobileMenuOpen = false"
          >
            عن المنصة
          </router-link>
          
          <router-link 
            to="/contact" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
            @click="mobileMenuOpen = false"
          >
            اتصل بنا
          </router-link>
          
          <router-link 
            to="/login" 
            class="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            active-class="text-primary-600"
            @click="mobileMenuOpen = false"
          >
            تسجيل الدخول
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'

const mobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}
</script> 