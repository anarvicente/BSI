/**
 * Created by ana on 20/10/16.
 */
public class Ex2 {

    public static boolean eh_primo(int n) /* retorna 0 se o numero nao for primo e 1 se for */
    {
        int primo, divisivel;
        boolean p;
        if(n == 1 || ((n != 2) && (n%2 == 0))) {  /* Verifica se o numero for diferente de 2 */
            primo = 0;		/* 2 eh o unico numero par primo */
            p = false;
        }
        else {                /* E se for par, entao nao eh primo */
            primo = 1;		/* Se nao, ha uma grande chance de ser no espaco dos impares */
            p = true;
        }
        divisivel = 3;      /* Comeca com 3 pq e o proximo numero primo */
        while(p && (divisivel <= Math.sqrt(n))){  /* Se primo e divisivel for menor ou igual a raiz quadrada do numero analisado */
            if(n%divisivel == 0) {           /* Se o resto da divisao do numero analisado pelo divisivel for 0 */
                primo = 0;				   /* Entao ele tem mais de dois divisores, nao eh primo */
                p = false;
            }

            divisivel = divisivel + 2;     /* Sendo primo ou nao, o divisivel aumenta em 2, soh anda nos impares */
        }
        return p;
    }

    public static void main(String [] args) {
        int i = 2, cont = 0;
        boolean n;
        while (cont < 5) {
            if(eh_primo(i)) {
                System.out.println(Math.pow(2, i - 1) * (Math.pow(2, i) - 1));
                cont++;
            }
            i++;

        }
    }
}
