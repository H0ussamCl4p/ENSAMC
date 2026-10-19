function d = distance(A, B)
    % Vérifie que A et B sont des vecteurs de même taille
    if ~isvector(A) || ~isvector(B)
        error('Les deux entrées doivent être des vecteurs.');
    end
    if length(A) ~= length(B)
        error('Les vecteurs doivent être de même longueur.');
    end

    % Assure que les vecteurs sont de même orientation (ligne ou colonne)
    A = A(:);  % convertit en vecteur colonne
    B = B(:);  % convertit en vecteur colonne

    % Calcule la distance euclidienne
    d = norm(A - B);
end
