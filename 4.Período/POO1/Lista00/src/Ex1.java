import java.util.Scanner;

/**
 * Created by ana on 20/10/16.
 */

import java.util.Scanner;

public class Ex1 {
   public static void main(String[] args){
       Scanner ler = new Scanner(System.in);
       String nome;
       int i=0;
       double qtd, soma = 0.0;

       System.out.println("Informe o seu nome: ");
       nome = ler.next();
       System.out.println("Informe a quantidade de provas que voce fez: ");
       qtd = ler.nextInt();
       while(i < qtd){
           System.out.println("Informe a nota da prova" + (i+1) + ": ");
           soma = soma + ler.nextDouble();
           i++;
       }
       System.out.println("Nome: " + nome);
       System.out.println("Media: " + soma/qtd);

   }
}
