import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    loading: false,
    error: null
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.user,
    currentUser: (state) => state.user,
    isLoading: (state) => state.loading,
    hasError: (state) => !!state.error
  },
  
  actions: {
    async login(credentials) {
      this.loading = true;
      this.error = null;
      
      try {
        // Simulate login with basic validation
        if (credentials.email && credentials.password) {
          const user = {
            id: Date.now(),
            email: credentials.email,
            firstName: 'Demo',
            lastName: 'User',
            username: credentials.email.split('@')[0]
          };
          
          this.user = user;
          localStorage.setItem('user', JSON.stringify(user));
          this.loading = false;
          return true;
        } else {
          throw new Error('Invalid credentials');
        }
      } catch (error) {
        this.loading = false;
        this.error = error.message || 'Login failed';
        return false;
      }
    },
    
    async register(userData) {
      this.loading = true;
      this.error = null;
      
      try {
        // Simulate registration
        if (userData.email && userData.password && userData.firstName && userData.lastName) {
          const user = {
            id: Date.now(),
            email: userData.email,
            firstName: userData.firstName,
            lastName: userData.lastName,
            username: userData.email.split('@')[0]
          };
          
          this.user = user;
          localStorage.setItem('user', JSON.stringify(user));
          this.loading = false;
          return true;
        } else {
          throw new Error('Please fill all required fields');
        }
      } catch (error) {
        this.loading = false;
        this.error = error.message || 'Registration failed';
        return false;
      }
    },
    
    logout() {
      this.user = null;
      localStorage.removeItem('user');
    },
    
    clearError() {
      this.error = null;
    }
  }
}); 