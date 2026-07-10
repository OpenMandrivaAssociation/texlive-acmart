%global tl_name acmart
%global tl_revision 79508

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.19
Release:	%{tl_revision}.1
Summary:	Class for typesetting publications of ACM
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/acmart
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a class for typesetting publications of the
Association for Computing Machinery (ACM).

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/acmart
%dir %{_datadir}/texmf-dist/doc/latex/acmart
%dir %{_datadir}/texmf-dist/source/latex/acmart
%dir %{_datadir}/texmf-dist/tex/latex/acmart
%dir %{_datadir}/texmf-dist/doc/latex/acmart/samples
%{_datadir}/texmf-dist/bibtex/bst/acmart/ACM-Reference-Format.bst
%doc %{_datadir}/texmf-dist/doc/latex/acmart/README
%doc %{_datadir}/texmf-dist/doc/latex/acmart/acm-jdslogo.png
%doc %{_datadir}/texmf-dist/doc/latex/acmart/acmart.bib
%doc %{_datadir}/texmf-dist/doc/latex/acmart/acmart.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/acmguide.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/Makefile
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/abbrev.bib
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmcp.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmcp.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmengage.dtx
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmengage.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmengage.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmlarge.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmlarge.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmmanuscript.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmmanuscript.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall-biblatex.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall-biblatex.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall-conf.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall-conf.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall-submission.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall-submission.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall-tagged.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall-tagged.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmsmall.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmtog-conf.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmtog-conf.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmtog.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/acmtog.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sample-base.bib
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sample-franklin.png
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/samples.dtx
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/samples.ins
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sampleteaser.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-authordraft.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-authordraft.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-biblatex.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-biblatex.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-i13n.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-i13n.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-lualatex.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-lualatex.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-tagged.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf-tagged.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigconf.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigplan.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/sigplan.tex
%doc %{_datadir}/texmf-dist/doc/latex/acmart/samples/software.bib
%doc %{_datadir}/texmf-dist/source/latex/acmart/Makefile
%doc %{_datadir}/texmf-dist/source/latex/acmart/acmart.dtx
%doc %{_datadir}/texmf-dist/source/latex/acmart/acmart.ins
%{_datadir}/texmf-dist/tex/latex/acmart/acmart.cls
%{_datadir}/texmf-dist/tex/latex/acmart/acmauthoryear.bbx
%{_datadir}/texmf-dist/tex/latex/acmart/acmauthoryear.cbx
%{_datadir}/texmf-dist/tex/latex/acmart/acmdatamodel.dbx
%{_datadir}/texmf-dist/tex/latex/acmart/acmnumeric.bbx
%{_datadir}/texmf-dist/tex/latex/acmart/acmnumeric.cbx
