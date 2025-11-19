def insertion_sort(array):
    #eu estou realmente puto de raiva com esse algoritmo, principalmente no que tange a parte da compreensão geral, mas em tese, eu entendo como ele funciona, mas que droga
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array
        

array = [2,3,1,5,6,7,3]
print(insertion_sort(array))
# achei completamente interessante o uso deste algoritmo e principalmente as suas aplicações no pior caso e no melhor caso, tendo em vista suas complexidades.
# No pior caso, quando o array está em ordem decrescente, a complexidade é O(n^2), pois cada elemento precisa ser comparado com todos os elementos anteriores.
# No melhor caso, quando o array já está ordenado, a complexidade é O(n), pois cada elemento só precisa ser comparado uma vez, sendo assim, algo constantemente linear.

