/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        custom: {
          "bg" : "#1D1A39",
          "headers": "#451952",
          "btns": "#662549",
          "accent": "#ff725e",
          "texto": "#F39F5A",
          "destacado": "#E8BCB9",
          "fondo-card": "#131126",
          "fondo-card-code": "#181530"
        }
      }
    },
  },
  plugins: [],
}

/*
#1D1A39 (Fondo de la web):
Este color es bastante oscuro, así que puede funcionar bien como fondo principal de tu página.

#451952 (Encabezados):
Puedes usar este color para resaltar los encabezados y títulos en tu página. Al ser un tono más oscuro pero aún vibrante, proporcionará un buen contraste con el fondo.

#662549 (Botones):
Este tono más oscuro puede ser ideal para los botones, ya que los hará destacar sin ser demasiado llamativos.

#AE445A (Acentos):
Utiliza este color para resaltar elementos importantes en tu página, como enlaces, iconos o elementos de navegación.

#F39F5A (Textos):
Este tono más claro puede ser útil para el texto principal de tu página, ya que es lo suficientemente legible pero aún así agrega un toque de color.

#E8BCB9 (Destacados):
Este color suave y claro puede ser útil para resaltar elementos secundarios o áreas de contenido especial en tu página.
*/