import { defineStore } from 'pinia';
import { profileService } from '@/services/api';

export const useProfileStore = defineStore('profile', {
  state: () => ({
    profile: null,
    preferences: null,
    potentialMatches: [],
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
        const response = await profileService.getMyProfile();
        this.profile = response.data;
        this.loading = false;
      } catch (error) {
        this.loading = false;
        this.error = error.response?.data || 'Failed to fetch profile';
      }
    },
    
    async updateProfile(profileData) {
      this.loading = true;
      
      try {
        const response = await profileService.updateProfile(profileData);
        this.profile = response.data;
        this.loading = false;
        return true;
      } catch (error) {
        this.loading = false;
        this.error = error.response?.data || 'Failed to update profile';
        return false;
      }
    },
    
    async fetchPreferences() {
      this.loading = true;
      
      try {
        const response = await profileService.getMatchPreferences();
        this.preferences = response.data.length > 0 ? response.data[0] : null;
        this.loading = false;
      } catch (error) {
        this.loading = false;
        this.error = error.response?.data || 'Failed to fetch preferences';
      }
    },
    
    async updatePreferences(preferencesData) {
      this.loading = true;
      
      try {
        let response;
        if (this.preferences) {
          preferencesData.id = this.preferences.id;
          response = await profileService.updatePreferences(preferencesData);
        } else {
          response = await profileService.updatePreferences(preferencesData);
        }
        
        this.preferences = response.data;
        this.loading = false;
        return true;
      } catch (error) {
        this.loading = false;
        this.error = error.response?.data || 'Failed to update preferences';
        return false;
      }
    },
    
    async fetchPotentialMatches() {
      this.loading = true;
      
      try {
        const response = await profileService.getPotentialMatches();
        this.potentialMatches = response.data;
        this.loading = false;
      } catch (error) {
        this.loading = false;
        this.error = error.response?.data || 'Failed to fetch potential matches';
      }
    },
    
    clearError() {
      this.error = null;
    }
  }
}); 