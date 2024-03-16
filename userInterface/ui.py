from extractor.cirurgiasPdfExtractor import extrair_texto
from looper.cirurgiasLooper import loop_pelas_cirurgias
from parser.cirurgias import extrair_data_das_cirurgias
from tkinter import filedialog, messagebox, ttk
from consts import surgeons
from tkinter import *
import webbrowser

def show_about():
    messagebox.showinfo("Sobre", "- Versão: 0.1")

def open_github():
    webbrowser.open("https://github.com/peusgarbi/hiorp")

def define_surgery_tag(surgeon: str) -> str:
    if surgeon in surgeons.we_do_all_surgeons:
        return "all"
    elif surgeon in surgeons.we_only_do_descriptions_surgeons:
        return "description"
    else:
        return "none"

def start_program() -> None:
    # Root
    root = Tk()
    root.title("Automatização HIORP")

    # Top Menu
    top_menu = Frame(root)
    top_menu.grid(column=0, row=0)

    about_button = Button(top_menu, text="Sobre", command=show_about)
    about_button.pack(side=RIGHT)

    github_button = Button(top_menu, text="GitHub", command=open_github)
    github_button.pack(side=LEFT)

    label_import_pdf = Label(root, text="Para iniciar, importe relatório do centro cirúrgico!")
    label_import_pdf.grid(column=0, row=1, padx=10, pady=20)
    
    def open_file():
        global selected_file
        file = filedialog.askopenfile(initialdir=CURRENT, filetypes=[("Arquivos PDF", "*.pdf")])
        selected_file = file

        selected_label = Label(root, text="Arquivo selecionado:")
        selected_label.grid(column=0, row=3, padx=10)

        file_label = Label(root, text=selected_file.name)
        file_label.grid(column=0, row=4, padx=10)

        surgeries_tree = ttk.Treeview(root, columns=("horario", "paciente", "idade", "nascimento", "cirurgiao", "acomodacao", "convenio", "servicos"), show="headings")
        surgeries_tree.heading("horario", text="Horário")
        surgeries_tree.column("horario", minwidth=46 , width=60)
        surgeries_tree.heading("paciente", text="Paciente")
        surgeries_tree.column("paciente", minwidth=100 , width=200)
        surgeries_tree.heading("idade", text="Idade")
        surgeries_tree.column("idade", minwidth=50 , width=60)
        surgeries_tree.heading("nascimento", text="Nascimento")
        surgeries_tree.column("nascimento", minwidth=50 , width=60)
        surgeries_tree.heading("cirurgiao", text="Cirurgião")
        surgeries_tree.column("cirurgiao", minwidth=100 , width=200)
        surgeries_tree.heading("acomodacao", text="Acomodação")
        surgeries_tree.column("acomodacao", minwidth=20 , width=40)
        surgeries_tree.heading("convenio", text="Convênio")
        surgeries_tree.column("convenio", minwidth=20 , width=40)
        surgeries_tree.heading("servicos", text="Serviços")
        surgeries_tree.column("servicos", minwidth=200 , width=400)

        pdf_full_text = extrair_texto(selected_file.name)
        surgeries_date = extrair_data_das_cirurgias(pdf_full_text)
        cirurgias = loop_pelas_cirurgias(pdf_full_text)

        file_label = Label(root, text=f"Data das cirurgias: {surgeries_date}")
        file_label.grid(column=0, row=5, padx=10)

        surgeries_tree.grid(column=0, row=6, padx=10)
        surgeries_tree.tag_configure("all", foreground="green")
        surgeries_tree.tag_configure("description", foreground="orange")
        surgeries_tree.tag_configure("none", foreground="red")

        sala1 = surgeries_tree.insert(parent="", index=END, values=("Sala 1",))
        for cirurgia in cirurgias.sala1:
            surgeries_tree.insert(parent=sala1, tags=(define_surgery_tag(cirurgia.cirurgiao),), index=END, values=(
                cirurgia.horario,
                cirurgia.paciente,
                cirurgia.idade,
                cirurgia.nascimento,
                cirurgia.cirurgiao,
                cirurgia.acomodacao,
                cirurgia.convenio,
                cirurgia.servicos,
            ))

        sala2 = surgeries_tree.insert(parent="", index=END, values=("Sala 2",))
        for cirurgia in cirurgias.sala2:
            surgeries_tree.insert(parent=sala2, tags=(define_surgery_tag(cirurgia.cirurgiao),), index=END, values=(
                cirurgia.horario,
                cirurgia.paciente,
                cirurgia.idade,
                cirurgia.nascimento,
                cirurgia.cirurgiao,
                cirurgia.acomodacao,
                cirurgia.convenio,
                cirurgia.servicos,
            ))

        sala3 = surgeries_tree.insert(parent="", index=END, values=("Sala 3",))
        for cirurgia in cirurgias.sala3:
            surgeries_tree.insert(parent=sala3, tags=(define_surgery_tag(cirurgia.cirurgiao),), index=END, values=(
                cirurgia.horario,
                cirurgia.paciente,
                cirurgia.idade,
                cirurgia.nascimento,
                cirurgia.cirurgiao,
                cirurgia.acomodacao,
                cirurgia.convenio,
                cirurgia.servicos,
            ))

        sala4 = surgeries_tree.insert(parent="", index=END, values=("Sala 4",))
        for cirurgia in cirurgias.sala4:
            surgeries_tree.insert(parent=sala4, tags=(define_surgery_tag(cirurgia.cirurgiao),), index=END, values=(
                cirurgia.horario,
                cirurgia.paciente,
                cirurgia.idade,
                cirurgia.nascimento,
                cirurgia.cirurgiao,
                cirurgia.acomodacao,
                cirurgia.convenio,
                cirurgia.servicos,
            ))

        sala5 = surgeries_tree.insert(parent="", index=END, values=("Sala 5",))
        for cirurgia in cirurgias.sala5:
            surgeries_tree.insert(parent=sala5, tags=(define_surgery_tag(cirurgia.cirurgiao),), index=END, values=(
                cirurgia.horario,
                cirurgia.paciente,
                cirurgia.idade,
                cirurgia.nascimento,
                cirurgia.cirurgiao,
                cirurgia.acomodacao,
                cirurgia.convenio,
                cirurgia.servicos,
            ))

    import_button = Button(root, text="Clique aqui para importar!", command=open_file)
    import_button.grid(column=0, row=2, pady=10)


    root.mainloop()
