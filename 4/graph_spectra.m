filename = 'example2.dat';

E = csvread(filename);
col1 = E(:,1);
col2 = E(:,2);
max_ids = max(max(col1,col2));
As = sparse(col1, col2, 1, max_ids, max_ids);
A  = full(As);

d = sum(A, 2);
D = diag(d);

% Plot Fiedler vector
% fied_L = D - A;
% [fied_vecs, fied_vals] = eigs(fied_L, size(A, 1)-1);
% fiedler_vec = fied_vecs(:, end-1);
% plot(sort(fiedler_vec));

% Partitioning
L = D ^ (-1/2) * A * D ^ (-1/2);
[vecs, vals] = eigs(L, size(A,1)-1); % Eigenvectors are on columns (1 column = 1 eigenvector)
k = 2;
X = vecs(:,1:k);
SS = arrayfun(@(n) norm(A(n,:)), 1:size(A,1));
Y = diag(1./SS) * X;
[idx, C, sumd] = kmeans(Y, k);

% Plot the partitions
G = graph(A);
p = plot(G);

colors = ['y' 'm' 'c' 'r' 'g' 'b' 'w' 'k'];
for label = 1:size(unique(idx), 1)
    color = colors(mod(label, size(colors, 2)) + 1);
    highlight(p, find(idx==label), 'NodeColor', color);
end
