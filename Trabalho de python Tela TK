import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename


class Aluno:
    def __init__(self, nome, matricula, nota1, nota2):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2


class CadastroNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Notas")
        self.root.configure(background='#1e5743')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=300)
        self.lista_alunos = []

        # Quadro dos campos de entrada
        self.frame_campos = tk.Frame(self.root, bd=2, relief=tk.SOLID)
        self.frame_campos.pack(padx=10, pady=10)

        self.label_nome = tk.Label(self.frame_campos, text="Nome do Aluno:", bg='#dfe3ee', fg='#107db2')
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.entry_nome = tk.Entry(self.frame_campos)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.label_matricula = tk.Label(self.frame_campos, text="Matrícula:", bg='#dfe3ee', fg='#107db2')
        self.label_matricula.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.entry_matricula = tk.Entry(self.frame_campos)
        self.entry_matricula.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.label_nota1 = tk.Label(self.frame_campos, text="Av1:", bg='#dfe3ee', fg='#107db2')
        self.label_nota1.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.entry_nota1 = tk.Entry(self.frame_campos)
        self.entry_nota1.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.label_nota2 = tk.Label(self.frame_campos, text="Av2:", bg='#dfe3ee', fg='#107db2')
        self.label_nota2.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        self.entry_nota2 = tk.Entry(self.frame_campos)
        self.entry_nota2.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        # Quadro dos botões
        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack(padx=10, pady=10)

        estilo_botao = {'bd': 2, 'bg': '#107db2', 'fg': 'white', 'font': ('verdana', 8, 'bold')}

        self.button_cadastrar = tk.Button(self.frame_botoes, text="Cadastrar", command=self.cadastrar_aluno,
                                          **estilo_botao)
        self.button_cadastrar.pack(side=tk.LEFT)

        self.button_excluir = tk.Button(self.frame_botoes, text="Excluir", command=self.excluir_aluno, **estilo_botao)
        self.button_excluir.pack(side=tk.LEFT)

        self.button_editar = tk.Button(self.frame_botoes, text="Editar", command=self.editar_aluno, **estilo_botao)
        self.button_editar.pack(side=tk.LEFT)

        self.button_buscar = tk.Button(self.frame_botoes, text="Buscar Arquivo", command=self.buscar_arquivo,
                                       **estilo_botao)
        self.button_buscar.pack(side=tk.LEFT)

        self.button_salvar = tk.Button(self.frame_botoes, text="Salvar Arquivo", command=self.salvar_arquivo,
                                       **estilo_botao)
        self.button_salvar.pack(side=tk.LEFT)

        # Tabela de exibição dos alunos
        self.tree_alunos = ttk.Treeview(self.root, columns=("Nome", "Matrícula", "Av1", "Av2"), show="headings")
        self.tree_alunos.pack(padx=10, pady=10)

        self.tree_alunos.heading("Nome", text="Nome")
        self.tree_alunos.heading("Matrícula", text="Matrícula")
        self.tree_alunos.heading("Av1", text="Av1")
        self.tree_alunos.heading("Av2", text="Av2")

        self.atualizar_tabela()

    def cadastrar_aluno(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        nota1 = self.entry_nota1.get()
        nota2 = self.entry_nota2.get()

        if nome and matricula and nota1 and nota2:
            aluno = Aluno(nome, matricula, nota1, nota2)
            self.lista_alunos.append(aluno)
            self.atualizar_tabela()
            self.limpar_campos()
            messagebox.showinfo("Cadastrar Aluno", "Aluno cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def excluir_aluno(self):
        selected_item = self.tree_alunos.selection()
        if selected_item:
            aluno_index = int(selected_item[0][1:]) - 1
            del self.lista_alunos[aluno_index]
            self.atualizar_tabela()
            messagebox.showinfo("Excluir Aluno", "Aluno excluído com sucesso!")
        else:
            messagebox.showerror("Erro", "Nenhum aluno selecionado!")

    def editar_aluno(self):
        selected_item = self.tree_alunos.selection()
        if selected_item:
            aluno_index = int(selected_item[0][1:]) - 1
            aluno = self.lista_alunos[aluno_index]
            self.entry_nome.delete(0, tk.END)
            self.entry_matricula.delete(0, tk.END)
            self.entry_nota1.delete(0, tk.END)
            self.entry_nota2.delete(0, tk.END)

            self.entry_nome.insert(0, aluno.nome)
            self.entry_matricula.insert(0, aluno.matricula)
            self.entry_nota1.insert(0, aluno.nota1)
            self.entry_nota2.insert(0, aluno.nota2)
        else:
            messagebox.showerror("Erro", "Nenhum aluno selecionado!")

    def buscar_arquivo(self):
        filename = askopenfilename(filetypes=[("Arquivo de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
        if filename:
            self.carregar_dados(filename)
            self.atualizar_tabela()
            messagebox.showinfo("Buscar Arquivo", "Arquivo carregado com sucesso!")

    def carregar_dados(self, filename):
        self.lista_alunos = []
        with open(filename, "r") as file:
            for line in file:
                nome, matricula, nota1, nota2 = line.strip().split(",")
                aluno = Aluno(nome, matricula, nota1, nota2)
                self.lista_alunos.append(aluno)

    def salvar_arquivo(self):
        filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])
        if filename:
            with open(filename, "w") as file:
                for aluno in self.lista_alunos:
                    file.write(f"{aluno.nome},{aluno.matricula},{aluno.nota1},{aluno.nota2}\n")
            messagebox.showinfo("Salvar Arquivo", "Arquivo salvo com sucesso!")

    def atualizar_tabela(self):
        for item in self.tree_alunos.get_children():
            self.tree_alunos.delete(item)

        for i, aluno in enumerate(self.lista_alunos, start=1):
            self.tree_alunos.insert("", tk.END, iid=f"aluno{i}", values=(aluno.nome, aluno.matricula,
                                                                          aluno.nota1, aluno.nota2))

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_nota1.delete(0, tk.END)
        self.entry_nota2.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    CadastroNotas(root)
    root.mainloop()
