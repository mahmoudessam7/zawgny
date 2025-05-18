/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#fef2f2',
          100: '#fee2e2',
          200: '#fecaca',
          300: '#fca5a5',
          400: '#f87171',
          500: '#ef4444',
          600: '#dc2626',
          700: '#b91c1c',
          800: '#991b1b',
          900: '#7f1d1d',
          950: '#450a0a',
        },
        secondary: {
          50: '#fefbf3',
          100: '#fcf4df',
          200: '#f9e8bf',
          300: '#f5d592',
          400: '#f0bc5e',
          500: '#eaa636',
          600: '#db852a',
          700: '#b66723',
          800: '#915223',
          900: '#764520',
          950: '#422411',
        },
        accent: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#0ea5e9',
          600: '#0284c7',
          700: '#0369a1',
          800: '#075985',
          900: '#0c4a6e',
          950: '#082f49',
        }
      },
      fontFamily: {
        arabic: ['Tajawal', 'sans-serif'],
      },
      backgroundImage: {
        'heart-pattern': "url('/images/heart-pattern.svg')",
        'wedding-texture': "url('/images/wedding-texture.svg')"
      }
    },
  },
  plugins: [],
} 