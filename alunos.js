const prompt = require('prompt-sync')()

let alunos = []
const menu = () => {
    console.log('MENU');
    console.log(' 1. adicionar aluno(a)\n 2. listar alunos\n 3. buscar aluno(a)\n 4. editar aluno(a)\n 5. exluir aluno(a)\n 6. sair');
    let escolha = prompt('Escolha uma opção: ');
    return escolha;
};

const add_alunos = (id) => {
    let nome = prompt('Nome do aluno(a): ');
    let notas = []
    for (let i = 1; i <= 3; i++) {
        let nota = parseFloat(prompt(`Nota ${i} do aluno(a): `));
        notas.push(nota);
    }

    console.log(`Aluno(a) ${nome} adicionado com sucesso!`)
    alunos.push({id: id, nome: nome, notas: notas = notas, media: (notas.reduce((acumulador, atual) => acumulador + atual, 0) / 3).toFixed(2)});
  
};

const listar_alunos = () => {
    for (let aluno of alunos) {
        console.log(`Aluno(a): ${aluno['nome']}, ID: ${aluno['id']}`);
        let quantidade = aluno['notas'].length 
        for (let i = 0; i < quantidade; i++) {
            console.log(`Nota ${i+1}: ${aluno['notas'][i]}`);
        }
        console.log(`Média: ${aluno['media']}`);
        console.log();
    }
};

const buscar_aluno = () => {
    let buscar_nome = prompt('Nome do aluno(a) que deseja procurar: ');
    let verificacao = false;
    for (let aluno of alunos) {
        if (buscar_nome.toLowerCase() == aluno['nome'].toLowerCase()) {
            console.log(`Aluno(a): ${aluno['nome']}`);
            verificacao = true;
            let quantidade = aluno['notas'].length 
            for (let i = 0; i < quantidade; i++) {
                console.log(`Nota ${i+1}: ${aluno['notas'][i]}`);
            }
        }
    }
    if (verificacao == false) {
        console.log(`Aluno(a) ${buscar_nome} não encontrado!`);
    }
};

const editar_aluno = () => {
    let modificar = prompt('O que deseja editar [1 -> nome do aluno(a), 2 -> notas do aluno(a)] ');
    console.log('Alunos cadastrados');
    let verificacao = false;
    let notas = []
    for (let aluno of alunos) {
        console.log(`Nome: ${aluno['nome']}, notas: ${aluno['notas']}`);
    }
    if (modificar == '1') { 
        let escolha_nome = prompt('Digite o nome do aluno: '); 
        for (let aluno of alunos) {
            if (escolha_nome.toLocaleLowerCase() == aluno['nome'].toLocaleLowerCase()) {
                nome_temporario = aluno['nome'];
                let novo_nome = prompt('Digite o nome certo: ');
                aluno['nome'] = novo_nome;
                verificacao = true;
                console.log('Mudança feita!');
                console.log(`${nome_temporario} -> ${novo_nome}`)
            }
        }
        if (verificacao == false) {
            console.log(`Aluno(a) ${escolha_nome} não encontrado!`)    
        }
    }
    else if (modificar == '2') {
        let escolha_nome = prompt('Nome do aluno(a) que você deseja mudar as notas: '); 
        for (let aluno of alunos) {
            if (escolha_nome.toLocaleLowerCase() == aluno['nome'].toLocaleLowerCase()) {
                verificacao = true
                for (let i = 1; i <= 3; i ++) {
                    let nota = parseFloat(prompt(`Nota ${i} do aluno(a): `))
                    notas.push(nota)
                }
                aluno['notas'] = notas
                let media = notas.reduce((acumulador, atual) => acumulador + atual, 0) / 3
                aluno['media'] = media.toFixed(2)
            }
        }
        if (verificacao == false) {
            console.log(`Aluno(a) ${escolha_nome} não encontrado!`)    
        }  
    }
};

const remover_aluno = () => {
    let verificacao = false
    for (let aluno of alunos) {
        console.log(`Nome: ${aluno['nome']}`);
    }
    let nome_aluno = prompt('Nome do aluno(a) que deseja remover: ')
    for (let aluno of alunos) {
        if (nome_aluno.toLocaleLowerCase() == aluno['nome'].toLocaleLowerCase()) {
            alunos = alunos.filter(aluno => aluno.nome.toLocaleLowerCase() !== nome_aluno.toLocaleLowerCase())
            verificacao = true
            console.log(`Aluno(a) ${nome_aluno} removido com sucesso!`)
        }
    }
    if (verificacao == false) {
        console.log(`Aluno(a) ${nome_aluno} não encontrado!`)
    }
}   

let id = 1;

while (true) {
    escolha = menu();
    if (escolha == '1') {
        add_alunos(id);
        id += 1;
    }
    else if (escolha == '2') {
        listar_alunos();
    }
    else if (escolha == '3') {
        buscar_aluno();
    }
    else if (escolha == '4') {
        editar_aluno();
    }
    else if (escolha == '5') {
        remover_aluno()
    }
    else if (escolha == '6') {
        console.log('Fim do programa!');
        break;
    }
    else {
        console.log('Opção inválida!');
    }
}