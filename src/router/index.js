import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/groom-register',
      name: 'groomRegister',
      component: () => import('../views/GroomRegisterView.vue')
    },
    {
      path: '/bride-register',
      name: 'brideRegister',
      component: () => import('../views/BrideRegisterView.vue')
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/ContactView.vue')
    },
    {
      path: '/terms',
      name: 'terms',
      component: () => import('../views/TermsView.vue')
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: () => import('../views/PrivacyView.vue')
    }
  ]
})

// Simple authentication guard for admin route
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    // This is a placeholder. In a real app, you'd check a token or session
    const isAdmin = localStorage.getItem('isAdmin') === 'true'
    if (!isAdmin) {
      next('/login')
      return
    }
  }
  next()
})

export default router
