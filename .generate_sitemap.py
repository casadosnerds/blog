import os
from datetime import datetime

# Configurações
site_url = "https://casadosnerds.github.io"
posts_folder = "."  # Pasta onde estão os posts
extensoes_validas = [".html", ".md"]

# Data de hoje
today = datetime.today().strftime('%Y-%m-%d')

# Início do sitemap
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n'

# Página principal
sitemap += "  <url>\n"
sitemap += f"    <loc>{site_url}/</loc>\n"
sitemap += f"    <lastmod>{today}</lastmod>\n"
sitemap += "    <changefreq>weekly</changefreq>\n"
sitemap += "    <priority>1.0</priority>\n"
sitemap += "  </url>\n\n"

# Lista arquivos de posts
for filename in os.listdir(posts_folder):
    name, ext = os.path.splitext(filename)
    if ext in extensoes_validas and name != "index":
        slug = name
        sitemap += "  <url>\n"
        sitemap += f"    <loc>{site_url}/{slug}</loc>\n"
        sitemap += f"    <lastmod>{today}</lastmod>\n"
        sitemap += "    <changefreq>monthly</changefreq>\n"
        sitemap += "    <priority>0.8</priority>\n"
        sitemap += "  </url>\n\n"

# Finaliza o sitemap
sitemap += '</urlset>'

# Escreve o arquivo
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print("Sitemap.xml gerado com sucesso!")