Name:		texlive-hep-math-font
Version:	67632
Release:	1
Summary:	Extended Greek and sans-serif math
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep-math-font
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math-font.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math-font.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math-font.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hep-math-font package adjust the math fonts to be
sans-serif if the document is sans-serif. Additionally Greek
letters are redefined to be always italic and upright in math
and text mode respectively. Some math font macros are adjusted
to give more consistently the naively expected results. The
package is loaded with \usepackage{hep-math-font}.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/hep-math-font
%{_texmfdistdir}/tex/latex/hep-math-font
%doc %{_texmfdistdir}/doc/fonts/hep-math-font

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
