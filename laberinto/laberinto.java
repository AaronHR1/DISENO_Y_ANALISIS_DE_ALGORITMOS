package laberinto;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class laberinto {
	public static void main(String[] args) {
        String ruta = "./entrada.txt"; 
        Array2d arreglo = null; 
        try (BufferedReader br = new BufferedReader(new FileReader(ruta))) {
        	
        	int filas = Integer.parseInt(br.readLine());
            int columnas = Integer.parseInt(br.readLine());
            
            //System.out.println(filas);
            //System.out.println(columnas);
            
            arreglo=new Array2d(filas,columnas);
            
            String linea;
            int i=0;
            
            while ((linea = br.readLine()) != null) {
            	int j=0;
            	int columna=0;
            	while(columna<columnas){
            		char c = linea.charAt(j);
            		if (c != ' ' && c != ',' && c != '\n') { 
        	        	arreglo.setItem(i, columna, c);
        	        	columna++;
        	        }
            		j++;
            	}
            	
            	i++;
            }
               
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        resolverLaberinto(arreglo);
        
    }
	
	public static void resolverLaberinto(Array2d arreglo){
		StackADT pila= new StackADT();
        int[] inicio = new int[2];
        for(int i=0;i<arreglo.getRowSize();i++){
            for(int j=0;j<arreglo.getColSize();j++){
                if(arreglo.getItem(i, j)=='E'){
                    inicio[0]=i;
                    inicio[1]=j;
                    break;
                }
            }
        }
       
        pila.push(inicio);
        int iteraciones=0;
        
        while(!pila.isEmpty()) {
        	   iteraciones++;
        	   int[] actual;
               
        	   actual=pila.peek();
               int fila=actual[0];
               int columna=actual[1];
               
               if(arreglo.getItem(fila,columna)== 'X' || arreglo.getItem(fila,columna)== '1'){
            	   pila.pop();
            	   continue;
               }
               
               if (arreglo.getItem(fila,columna) == 'S') {
            	   System.out.println("salida encontrada en "  + fila + " " + columna);
            	   
            	   while(!pila.isEmpty()) {
            		   int[] camino = (int[]) pila.pop();
            		   int filaCamino = camino[0];
            		   int columnaCamino = camino[1];
            		   
            		   if(arreglo.getItem(filaCamino, columnaCamino)!= 'E' && arreglo.getItem(filaCamino, columnaCamino)!= 'S') {
            			   
            			   arreglo.setItem(filaCamino, columnaCamino, 'C');
            		   }
            		   
            	   }
            	   
            	   for (int i = 0; i < arreglo.getRowSize(); i++) {
                       for (int j = 0; j < arreglo.getColSize(); j++) {
                           System.out.print(arreglo.getItem(i, j) + " ");
                       }
                       System.out.println();
                   }
                   return;
            	   
               }
               
               if (arreglo.getItem(fila,columna) != 'E' && arreglo.getItem(fila,columna) != 'S') {
            	    arreglo.setItem(fila, columna, 'X');
               }
               boolean flag=false;
               
               if(esValido(fila+1,columna,arreglo)) {pila.push(new int[] {fila+1,columna});
               		flag=true;
               }
   
               else if(esValido(fila-1,columna,arreglo)) {pila.push(new int[] {fila-1,columna});
          			flag=true;
               }
               
               else if(esValido(fila,columna+1,arreglo)) { pila.push(new int[] {fila,columna+1});
          			flag=true;
               }
               
               else if(esValido(fila,columna-1,arreglo)) { pila.push(new int[] {fila,columna-1});
          			flag=true;
               }
               
               if(!flag) {
            	   pila.pop();
                   
               }
        }
        
        
        
	}
	
	public static boolean esValido(int fila,int columna,Array2d arreglo) {
		if(fila<arreglo.getRowSize() && columna<arreglo.getColSize() && fila>=0 && columna>=0 && arreglo.getItem(fila, columna) == '0' || arreglo.getItem(fila, columna) == 'S') {
			return true;
		}
		return false;
	}
	

}
