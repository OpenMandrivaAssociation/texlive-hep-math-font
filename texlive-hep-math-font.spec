%global tl_name hep-math-font
%global tl_revision 76220

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Extended Greek and sans-serif math
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/hep-math-font
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math-font.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math-font.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math-font.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The hep-math-font package adjust the math fonts to be sans-serif if the
document is sans-serif. Additionally Greek letters are redefined to be
always italic and upright in math and text mode respectively. Some math
font macros are adjusted to give more consistently the naively expected
results. The package is loaded with \usepackage{hep-math-font}.

