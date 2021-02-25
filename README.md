# Eye Tracker Setup

<img src="https://www.groovypost.com/wp-content/uploads/2017/08/Tobii-Eye-Tracker.png" width="100%" />

Setup screen [Tobii Eye Tracker 4C](https://gaming.tobii.com/product/tobii-eye-tracker-4c/) gazing information for [usability testing](https://github.com/MIMBCD-UI/prototype-breast-screening/wiki/User-Research#user-test-evaluations-) purpose. The [Tobii Eye Tracker 4C](https://gaming.tobii.com/product/tobii-eye-tracker-4c/) aims at providing an immersive reality without a headset. Also, with this product nothing stands between the screen and the immersive experience. Therefore, our clinicians will work with no interference of the device. This repository includes functions for the setup os the eye-tracking routines including: (i) calibration of the eye-tracker; (ii) finding eye positions; and (iii) validation of eye-tracker calibration settings. It contains functions for working with with the new [Tobii Pro SDK](https://www.tobiipro.com/product-listing/tobii-pro-sdk/) for [Python](http://developer.tobiipro.com/python.html), along with essential Eye-Tracking routines, in a `TobiiHelper` class. The repository is part of the work done by [SIPg](http://sipg.isr.tecnico.ulisboa.pt/), an [ISR-Lisboa](http://welcome.isr.tecnico.ulisboa.pt/) research group and [M-ITI](https://www.m-iti.org/), two [R&D Units](http://larsys.pt/index.php/facilities/) of [LARSyS](http://larsys.pt/). The project also involves the collaborative effort of [INESC-ID](http://www.inesc-id.pt/). Both [ISR-Lisboa](http://welcome.isr.tecnico.ulisboa.pt/) and [INESC-ID](http://www.inesc-id.pt/) are [Associate Laboratories](https://tecnico.ulisboa.pt/en/research-and-innovation/rd/associate-laboratories/) of [IST](http://tecnico.ulisboa.pt/) from [ULisboa](https://www.ulisboa.pt/).


## Citing

We kindly ask **scientific works and studies** that make use of the repository to cite it in their associated publications. Similarly, we ask **open-source** and **closed-source** works that make use of the repository to warn us about this use.

You can cite our work using the following BibTeX entry:

```
@article{CALISTO2021102607,
title = {Introduction of human-centric AI assistant to aid radiologists for multimodal breast image classification},
journal = {International Journal of Human-Computer Studies},
volume = {150},
pages = {102607},
year = {2021},
issn = {1071-5819},
doi = {https://doi.org/10.1016/j.ijhcs.2021.102607},
url = {https://www.sciencedirect.com/science/article/pii/S1071581921000252},
author = {Francisco Maria Calisto and Carlos Santiago and Nuno Nunes and Jacinto C. Nascimento},
keywords = {Human-computer interaction, Artificial intelligence, Healthcare, Medical imaging, Breast cancer},
abstract = {In this research, we take an HCI perspective on the opportunities provided by AI techniques in medical imaging, focusing on workflow efficiency and quality, preventing errors and variability of diagnosis in Breast Cancer. Starting from a holistic understanding of the clinical context, we developed BreastScreening to support Multimodality and integrate AI techniques (using a deep neural network to support automatic and reliable classification) in the medical diagnosis workflow. This was assessed by using a significant number of clinical settings and radiologists. Here we present: i) user study findings of 45 physicians comprising nine clinical institutions; ii) list of design recommendations for visualization to support breast screening radiomics; iii) evaluation results of a proof-of-concept BreastScreening prototype for two conditions Current (without AI assistant) and AI-Assisted; and iv) evidence from the impact of a Multimodality and AI-Assisted strategy in diagnosing and severity classification of lesions. The above strategies will allow us to conclude about the behaviour of clinicians when an AI module is present in a diagnostic system. This behaviour will have a direct impact in the clinicians workflow that is thoroughly addressed herein. Our results show a high level of acceptance of AI techniques from radiologists and point to a significant reduction of cognitive workload and improvement in diagnosis execution.}
}
```

## Pre-Requisites

The following list is showing the set of dependencies for this project. Please, install and build in your machine the recommended versions.

List of dependencies for this project:

- [Git](https://git-scm.com/) (>= [v2.20](https://raw.githubusercontent.com/git/git/master/Documentation/RelNotes/2.20.1.txt))

- [Python](https://www.python.org/) (>= [v2.7](https://docs.python.org/2/))

- [Setuptools](https://pypi.org/project/setuptools/) (>= [v40.8](https://pypi.org/project/setuptools/40.8.0/))

- [Tobii Research](https://pypi.org/project/tobii-research/) (>= [v1.6](https://pypi.org/project/tobii-research/1.6.1/))

### Analytical Use

Tobii’s consumer eye trackers are primarily intended for personal interaction use and not for analytical purposes. Any application that stores or transfers eye tracking data must have a special license from Tobii ([Read more](https://analyticaluse.tobii.com/)). Please, apply for a license [here](https://analyticaluse.tobii.com/license-application-form/).

## Instructions

The instructions are as follows. We assume that you already have knowledge over [Git](https://git-scm.com/) and [GitHub](https://github.com/). If not, please follow this [support](https://guides.github.com/activities/hello-world/) information. Any need for support, just open a [New issue](https://github.com/mida-project/eye-tracker-setup/issues/new).

### Clone

To clone the hereby repository follow the guidelines. It is easy as that.

1.1. Please clone the repository by typing the command:

```
git clone https://github.com/mida-project/eye-tracker-setup.git
```

1.2. Get inside of the repository directory:

```
cd eye-tracker-setup/
```

1.3. For the installation and running of the source code, follow the next steps;

### Install

The installation guidelines are as follows. Please, be sure that you follow it correctly.

2.1. Run the following command to install the [library](http://docs.python-requests.org/en/master/user/install/#install) using [pip](https://pypi.org/project/pip/):

#### On Linux or OS X

```
pip install -U pip setuptools
pip install tobii-research
```

#### On Windows

```
python -m pip install -U pip setuptools
pip install tobii-research
```

2.2. Follow the next step;

### Run

The running guidelines are as follows. Please, be sure that you follow it correctly.

3.1. Run the sample using the following command:

```
python2 src/core/main.py
```

3.2. Enjoy our source code!

### Notebooks

You can also run a Notebook to watch some of our `models` chart plots. For this goal we are using the well known [Jupyter Notebook](http://jupyter.org/) web application. To run the [Jupyter Notebook](http://jupyter.org/) just follow the steps.

4.1. Get inside our project directory:

```
cd eye-tracker-setup/src/notebooks/
```

4.2. Run [Jupyter Notebook](http://jupyter.org/) application by typing:

```
jupyter notebook
```

> If you have any question regarding the [Jupyter Notebook](http://jupyter.org/) just follow their [Documentation](http://jupyter.org/documentation). You can also ask for help close to the [Community](http://jupyter.org/community).

## Information

To find out how to apply the [Upgrade Key](https://www.tobiipro.com/siteassets/tobii-pro/product-descriptions/tobii-pro-upgrade-key-product-description.pdf/?v=1.5) to a [Tobii Eye Tracker 4C](https://gaming.tobii.com/product/tobii-eye-tracker-4c/), follow the [Tobii Pro Upgrade Key – User Instructions](https://www.tobiipro.com/siteassets/tobii-pro/user-manuals/tobii-pro-upgrade-key-user-instructions.pdf/?v=1.1) document. Nevertheless, the [Tobii Pro SDK Python API Documentation](http://devtobiipro.azurewebsites.net/tobii.research/python/reference/1.6.1.22-alpha-g9a43723/index.html) page is of chief importance to this repository, as well as, their [Examples](http://devtobiipro.azurewebsites.net/tobii.research/python/reference/1.6.1.22-alpha-g9a43723/examples.html) page for [Python](http://developer.tobiipro.com/python.html). For the first configurations, please follow both [Python - Getting started](http://developer.tobiipro.com/python/python-getting-started.html) and [Python - Step-by-step guide](http://developer.tobiipro.com/python/python-step-by-step-guide.html) pages, or follow the presented steps. Any questions regarding the [Eye-Tracking topic](https://en.wikipedia.org/wiki/Eye_tracking) just follow the [StackOverflow tag](https://stackoverflow.com/questions/tagged/eye-tracking) for the purpose.

### Acknowledgements

The work is also based and highly contributed from the [`tobii_pro_wrapper`](https://github.com/oguayasa/tobii_pro_wrapper). The [`tobii_pro_wrapper`](https://github.com/oguayasa/tobii_pro_wrapper) repository was developed by [Olivia Guayasamin](http://collectivebehaviour.com/) ([oguayasa](https://github.com/oguayasa)) that we would like to thank. That repository shows pretty much everything we need to connect to a Tobii Eye-Tracker, calibrate the eyetracker, get gaze, eye, and time synchronization data from the eyetracker device, and convert the Tobii coordinate systems units.

### Authors

- [Francisco Maria Calisto](http://www.franciscocalisto.me/) [[ResearchGate](https://www.researchgate.net/profile/Francisco_Maria_Calisto) | [GitHub](https://github.com/FMCalisto) | [Twitter](https://twitter.com/FMCalisto) | [LinkedIn](https://www.linkedin.com/in/fmcalisto/)]

## Sponsors

<span class="image">
  <a href="http://www.fct.pt/" title="FCT" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/fct_footer.png" alt="fct" width="20%" />
  </a>
</span>
<span class="image">
  <a href="https://www.fccn.pt/en/" title="FCCN" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/fccn_footer.png" alt="fccn" width="20%" />
  </a>
</span>
<span class="image">
  <a href="https://www.ulisboa.pt/en/" title="ULisboa" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/ulisboa_footer.png" alt="ulisboa" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://tecnico.ulisboa.pt/" title="IST" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/ist_footer.png" alt="ist" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://hff.min-saude.pt/" title="HFF" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/hff_footer.png" alt="hff" width="20%" />
  </a>
</span>

## Departments

<span class="image">
  <a href="http://dei.tecnico.ulisboa.pt" title="DEI" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/dei_footer.png" alt="dei" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://deec.tecnico.ulisboa.pt" title="DEEC" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/deec_footer.png" alt="dei" width="20%" />
  </a>
</span>

## Laboratories

<span class="image">
  <a href="http://sipg.isr.tecnico.ulisboa.pt/" title="SIPG" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/sipg_footer.png" alt="sipg" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://welcome.isr.tecnico.ulisboa.pt/" title="ISR" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/isr-lisboa_footer.png" alt="isr" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://larsys.pt/" title="LARSys" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/larsys_footer.png" alt="larsys" width="20%" />
  </a>
</span>
<span class="image">
  <a href="https://www.m-iti.org/" title="M-ITI" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/miti_footer.png" alt="inesc-id" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://www.inesc-id.pt/" title="INESC-ID" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/inesc-id_footer.png" alt="inesc-id" width="20%" />
  </a>
</span>

## Domain

<span class="image">
  <a href="https://europa.eu/" title="EU" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/eu_footer.png" alt="eu" width="20%" />
  </a>
</span>
<span class="image">
  <a href="https://www.portugal.gov.pt/" title="Portugal" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/pt_footer.png" alt="pt" width="20%" />
  </a>
</span>
