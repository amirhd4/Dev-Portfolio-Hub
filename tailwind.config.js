/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        'midnight-navy': '#0a192f',
        'space-blue': '#112240',
        'misty-white': '#ccd6f6',
        'slate-gray': '#8892b0',
        'neon-teal': '#64ffda',
      },
      fontFamily: {
        'sans': ['Manrope', 'sans-serif'],
        'serif': ['Playfair Display', 'serif'],
        'mono': ['Fira Code', 'monospace'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}