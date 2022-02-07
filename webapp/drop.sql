INSERT INTO public.article_types (id, "type") VALUES(1, 'news');
INSERT INTO public.article_types (id, "type") VALUES(2, 'tech');
INSERT INTO public.article_types (id, "type") VALUES(3, 'entertainment');

INSERT INTO public.author (id, author) VALUES(1, 'Chappie');
INSERT INTO public.author (id, author) VALUES(2, 'Wall-e');
INSERT INTO public.author (id, author) VALUES(3, 'Atom');
INSERT INTO public.author (id, author) VALUES(4, 'T1000');

INSERT INTO public.magazines (id, "name") VALUES(1, 'it herald');
INSERT INTO public.magazines (id, "name") VALUES(2, 'IT STORIES');
INSERT INTO public.magazines (id, "name") VALUES(3, 'IT with kids');

INSERT INTO public.articles (id, magazine_id, article_type_id, author_id) VALUES(1, 1, 2, 3);
INSERT INTO public.articles (id, magazine_id, article_type_id, author_id) VALUES(2, 3, 3, 2);
INSERT INTO public.articles (id, magazine_id, article_type_id, author_id) VALUES(3, 2, 2, 4);
INSERT INTO public.articles (id, magazine_id, article_type_id, author_id) VALUES(4, 1, 1, 1);

SELECT setval('article_types_id_seq', (SELECT MAX(id) from article_types), true);
SELECT setval('author_id_seq', (SELECT MAX(id) from author), true);
SELECT setval('magazines_id_seq', (SELECT MAX(id) from magazines), true);
SELECT setval('articles_id_seq', (SELECT MAX(id) from articles), true);
