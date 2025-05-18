import axios from 'axios';

// Backend API URL (assuming both are running on the same host)
const API_URL = 'http://localhost:8000/api/';

const apiClient = axios.create({
  baseURL: API_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
});

// Add token to requests if available
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

// Auth services
export const authService = {
  register(userData) {
    return apiClient.post('register/', userData);
  },
  
  login(credentials) {
    return apiClient.post('login/', credentials);
  },
  
  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  },
  
  getCurrentUser() {
    return JSON.parse(localStorage.getItem('user'));
  },
  
  setUser(userData, token) {
    localStorage.setItem('user', JSON.stringify(userData));
    localStorage.setItem('token', token);
  }
};

// Profile services
export const profileService = {
  getMyProfile() {
    return apiClient.get('profiles/my_profile/');
  },
  
  updateProfile(profileData) {
    return apiClient.patch(`profiles/${profileData.id}/`, profileData);
  },
  
  getMatchPreferences() {
    return apiClient.get('preferences/');
  },
  
  updatePreferences(prefData) {
    if (prefData.id) {
      return apiClient.patch(`preferences/${prefData.id}/`, prefData);
    } else {
      return apiClient.post('preferences/', prefData);
    }
  },
  
  getPotentialMatches() {
    return apiClient.get('profiles/potential_matches/');
  }
};

// Match request services
export const matchService = {
  getMyMatchRequests() {
    return apiClient.get('match-requests/');
  },
  
  sendMatchRequest(receiverId, message) {
    return apiClient.post('match-requests/', {
      receiver: receiverId,
      message: message
    });
  },
  
  acceptRequest(requestId) {
    return apiClient.post(`match-requests/${requestId}/accept/`);
  },
  
  rejectRequest(requestId) {
    return apiClient.post(`match-requests/${requestId}/reject/`);
  }
};

// Conversation and messaging services
export const messageService = {
  getMyConversations() {
    return apiClient.get('conversations/');
  },
  
  getMessages(conversationId) {
    return apiClient.get(`messages/?conversation=${conversationId}`);
  },
  
  sendMessage(conversationId, content) {
    return apiClient.post('messages/', {
      conversation: conversationId,
      content: content
    });
  }
};

export default {
  authService,
  profileService,
  matchService,
  messageService
}; 