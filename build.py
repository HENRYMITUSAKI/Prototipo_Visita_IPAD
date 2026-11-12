from pathlib import Path
root=Path(__file__).resolve().parent
css=(root/'src/styles.css').read_text()
js='\n'.join((root/f'src/{name}.js').read_text() for name in ['data','core','report','ui'])
html='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#123d49"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Ronda"><link rel="manifest" href="./manifest.webmanifest"><link rel="apple-touch-icon" href="./icon-192.png"><title>Ronda · Visita de enfermagem v3</title><style>'''+css+'''</style></head><body><div id="app"></div><script>'''+js+'''</script></body></html>'''
(root/'index.html').write_text(html)
print('index.html gerado:',len(html.encode()),'bytes')
