# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build

from cx_Freeze import setup, Executable

executables = [
        Executable(
        script ="stationnement_final.py",
##        icon='nom.ico',
##        base = 'Win32GUI'
        )
]

# ne pas mettre "base = ..." si le programme n'est pas en mode graphique,
# comme c'est le cas pour chiffrement.py.

buildOptions = dict(
                includes = [
                            "tkinter ",
                            "tkinter.font",
                            "pandas",
                            "numpy",
                            "scipy",
                            "matplotlib",
                            "matplotlib.pyplot",
                            "googlemaps",
                            "gmplot",
                            "webbrowser",
                            "easygui ",
                            "matplotlib.backends.backend_tkagg"
                            "matplotlib.figure"
                            ],
                include_files = [
                                "df_clean.csv",
                                "dfq1.csv",
                                "dfq2.csv",
                                "dfq3.csv",
                                "nettoyage_donnees.ipynb",
                                "resultat_final.ipynb",
                                "paris.png",
                                "parking.png",
                                "q1.png",
                                "q2.png",
                                "q3.png",
                                "setup.py",
                                "stationnement_final.py",
                                "stationnements.txt",
                                ]
                )


setup(
    name = "nom_du_programme",
    version = "1.2",
    description = "",
    author = "votre nom",
    options = dict(huild_exe = buildOptions),
    executables = executables
    )