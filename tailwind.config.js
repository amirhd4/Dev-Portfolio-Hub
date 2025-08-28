/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',
    './apps/**/*.{html,js,py}',
    './static/src/**/*.{js,jsx,ts,tsx}',
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
        'sans': ['Vazirmatn', 'sans-serif'],
        'serif': ['Playfair Display', 'serif'],
        'mono': ['Fira Code', 'monospace'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),

  ],
}
