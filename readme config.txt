echo "# mis-catalogos" >> README.md
git config --global user.name "Uvero"
git config --global user.email "uvero.alto.3@gmail.com"
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Uvero/mi-catalogo.git
git push -u origin main