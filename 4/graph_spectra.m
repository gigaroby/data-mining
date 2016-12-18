filename = 'example1.dat';

E = csvread(filename);
col1 = E(:,1);
col2 = E(:,2);
max_ids = max(max(col1,col2));
As = sparse(col1, col2, 1, max_ids, max_ids);
A  = full(As);

d = sum(A, 2);
D = diag(d);

L = D ^ (-1/2) * A * D ^ (-1/2);
%L = D - A;
% [vecs, vals] = eig(L);  % eigenvectors are on columns (1 column = 1 eigenvector)
[vecs, vals] = eigs(L, size(A,1)-1);
% ds_vecs = fliplr(vecs);
ds_vecs = vecs;
k = 4;
X = ds_vecs(:,1:k);
SS = arrayfun(@(n) norm(A(n,:)), 1:size(A,1));
Y = diag(1./SS) * X;
idx = kmeans(Y, k);

% plot
G = graph(A);
p = plot(G);

colors = ['y' 'm' 'c' 'r' 'g' 'b' 'w' 'k'];
for label = 1:size(unique(idx), 1)
    color = colors(mod(label, size(colors, 2)) + 1);
    highlight(p, find(idx==label), 'NodeColor', color);
end
