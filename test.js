let objeto = {
    nome: 'josé',
    notas: notas = [4, 5, 7],
    media: (notas.reduce((acumulador, atual) => acumulador + atual, 0) /3).toFixed(2)
};
objeto['notas'][2] = 5;
objeto['media'] = (notas.reduce((acumulador, atual) => acumulador + atual, 0) /3).toFixed(2)
console.log(objeto);
delete objeto.nome
delete objeto.notas
delete objeto.media
console.log(objeto)