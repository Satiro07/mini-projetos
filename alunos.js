const prompt = require('prompt-sync')();

let alunos = [];
function menu() {
    console.log('MENU');
    console.log(' 1. adicionar aluno\n 2. listar alunos');
    let escolha = prompt('Escolha uma opção: ');
    return escolha;
};

function add_alunos () {
    let nome = prompt('Nome do aluno: ');
    let notas = []
    for (let i = 1; i <= 3; i++) {
        let nota = parseFloat(prompt(`Nota ${i} do aluno: `));
        notas.push(nota);
    }
    console.log(`Aluno ${nome} adicionado com sucesso!`)
    alunos.push({nome: notas});
};

function listar_alunos () {
    for (let aluno of Object.keys(alunos)) {
        console.log(aluno['nome']);
        for (let aluno of Object.values(alunos)) {
            console.log(aluno)
        }
    }
};

while (true) {
    
    escolha = menu();
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
