import { defineStore } from 'pinia';
import { authService } from '@/services/api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
    loading: false,
    error: null
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.token,
    currentUser: (state) => state.user,
    isLoading: (state) => state.loading,
    hasError: (state) => !!state.error
  },
  
  actions: {
    async login(credentials) {
      this.loading = true;
      this.error = null;
      
      try {
        const response = await authService.login(credentials);
        this.token = response.data.token;
        this.user = {
          id: response.data.user_id,
          username: response.data.username,
          email: response.data.email,
          firstName: response.data.first_name,
          lastName: response.data.last_name
        };
        
        authService.setUser(this.user, this.token);
        this.loading = false;
        return true;
      } catch (error) {
        this.loading = false;
        this.error = error.response?.data || 'Login failed';
        return false;
      }
    },
    
    async register(userData) {
      this.loading = true;
      this.error = null;
      
      try {
        await authService.register(userData);
        this.loading = false;
        return true;
      } catch (error) {
        this.loading = false;
        this.error = error.response?.data || 'Registration failed';
        return false;
      }
    },
    
    async fetchCurrentUser() {
      if (!this.token) return;
      
      this.loading = true;
      
      try {
        const response = await authService.getMyProfile();
        this.user = response.data;
        this.loading = false;
      } catch (error) {
        this.loading = false;
        if (error.response?.status === 401) {
          this.logout();
        }
      }
    },
    
    logout() {
      this.user = null;
      this.token = null;
      authService.logout();
    },
    
    clearError() {
      this.error = null;
    }
  }
}); 