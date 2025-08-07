/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/*.py',
],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Vazirmatn', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

