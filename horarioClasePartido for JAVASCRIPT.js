class HorarioMedicamento {
  constructor(nombrePaciente, nombreMedicamento, horaInicial) {
    this.nombrePaciente = nombrePaciente;
    this.nombreMedicamento = nombreMedicamento;
    this.horaInicial = horaInicial;
    this.contador = 1;
    this.horaTomarMedicamento = this.horaInicial;
  }

  horarioParaTomarMedicamento() {
    while (this.contador < 10) {
      if (this.horaTomarMedicamento >= 24) {
        this.horaTomarMedicamento = this.horaTomarMedicamento - 24;
      }

      this.imprimirHoraTomarMedicamento();
      this.calcularHoraTomarMedicamento();
      this.aumentarContador();
    }
    console.log("Finalizo su tratamiento");
  }

  imprimirHoraTomarMedicamento() {
    console.log(
      `Toma numero ${this.contador} de su tratamiento: Debe toma su medicamento a las ${this.horaTomarMedicamento}h`
    );
  }

  calcularHoraTomarMedicamento() {
    this.horaTomarMedicamento = this.horaTomarMedicamento + 8;
  }

  aumentarContador() {
    this.contador = this.contador + 1;
  }
}

const paciente1 = new HorarioMedicamento("Pepito", "Dolex", 8);
paciente1.imprimirHoraTomarMedicamento();
paciente1.calcularHoraTomarMedicamento();
paciente1.aumentarContador();
console.log(paciente1.horarioParaTomarMedicamento());
