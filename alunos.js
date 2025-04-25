const prompt = require('prompt-sync')();

let alunos = [];
function menu(esc) {
    console.log('MENU');
    console.log(' 1. adicionar aluno\n 2. listar alunos');
    let escolha = prompt('Escolha uma opção: ');
    return escolha
};

function add_alunos () {
    let nome = prompt('Nome do aluno: ');
    let notas = []
    for (let i = 1; i <= 3; i++) {
        let nota = parseFloat(prompt(`Nota ${i} do aluno: `));
        notas.push(nota);
    }
    console.log(`Aluno ${nome} adicionado com sucesso!`)
    alunos.push({nome: nome, notas: notas});
};

function listar_alunos () {
    for (let aluno of alunos) {
        console.log(aluno);
    }
};

while (true) {
    escolha = menu(e);
    if (escolha == '1') {
        add_alunos();
    }
    else if (escolha == '2') {
        listar_alunos();
    }
    else {
        break;
    }
}
