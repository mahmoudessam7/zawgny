import { defineStore } from 'pinia';

export const useProfileStore = defineStore('profile', {
  state: () => ({
    profile: JSON.parse(localStorage.getItem('profile')) || null,
    preferences: JSON.parse(localStorage.getItem('preferences')) || null,
    potentialMatches: JSON.parse(localStorage.getItem('potentialMatches')) || [],
    loading: false,
    error: null
  }),
  
  getters: {
    hasProfile: (state) => !!state.profile,
    hasPreferences: (state) => !!state.preferences,
    isLoading: (state) => state.loading,
    hasError: (state) => !!state.error
  },
  
  actions: {
    async fetchMyProfile() {
      this.loading = true;
      
      try {
        // Simulate fetching profile data
        await new Promise(resolve => setTimeout(resolve, 500));
        
        if (!this.profile) {
          this.profile = {
            id: Date.now(),
            age: 25,
            gender: '',
            bio: '',
            location: '',
            interests: [],
            photos: []
          };
          localStorage.setItem('profile', JSON.stringify(this.profile));
        }
        
        this.loading = false;
      } catch (error) {
        this.loading = false;
        this.error = error.message || 'Failed to fetch profile';
      }
    },
    
    async updateProfile(profileData) {
      this.loading = true;
      
      try {
        // Simulate profile update
        await new Promise(resolve => setTimeout(resolve, 500));
        
        this.profile = { ...this.profile, ...profileData };
        localStorage.setItem('profile', JSON.stringify(this.profile));
        
        this.loading = false;
        return true;
      } catch (error) {
        this.loading = false;
        this.error = error.message || 'Failed to update profile';
        return false;
      }
    },
    
    async fetchPreferences() {
      this.loading = true;
      
      try {
        // Simulate fetching preferences
        await new Promise(resolve => setTimeout(resolve, 500));
        
        if (!this.preferences) {
          this.preferences = {
            id: Date.now(),
            minAge: 18,
            maxAge: 35,
            preferredGender: '',
            maxDistance: 50,
            interests: []
          };
          localStorage.setItem('preferences', JSON.stringify(this.preferences));
        }
        
        this.loading = false;
      } catch (error) {
        this.loading = false;
        this.error = error.message || 'Failed to fetch preferences';
      }
    },
    
    async updatePreferences(preferencesData) {
      this.loading = true;
      
      try {
        // Simulate preferences update
        await new Promise(resolve => setTimeout(resolve, 500));
        
        this.preferences = { ...this.preferences, ...preferencesData };
        localStorage.setItem('preferences', JSON.stringify(this.preferences));
        
        this.loading = false;
        return true;
      } catch (error) {
        this.loading = false;
        this.error = error.message || 'Failed to update preferences';
        return false;
      }
    },
    
    async fetchPotentialMatches() {
      this.loading = true;
      
      try {
        // Simulate fetching potential matches
        await new Promise(resolve => setTimeout(resolve, 500));
        
        if (this.potentialMatches.length === 0) {
          // Generate some mock data for demo purposes
          this.potentialMatches = [
            {
              id: 1,
              name: 'Sarah Johnson',
              age: 28,
              bio: 'Love hiking and photography',
              location: 'Cairo',
              photos: []
            },
            {
              id: 2,
              name: 'Ahmed Hassan',
              age: 32,
              bio: 'Software engineer passionate about technology',
              location: 'Alexandria',
              photos: []
            }
          ];
          localStorage.setItem('potentialMatches', JSON.stringify(this.potentialMatches));
        }
        
        this.loading = false;
      } catch (error) {
        this.loading = false;
        this.error = error.message || 'Failed to fetch potential matches';
      }
    },
    
    clearError() {
      this.error = null;
    }
  }
}); 