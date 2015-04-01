;; Configuration variables here:
(global-set-key  [f11] 'gud-step)
(global-set-key  [f10] 'gud-next)
(global-set-key  [f7] 'compile)
(global-set-key  [f5] 'gud-cont)
(global-set-key  [f6] 'gdb)
(global-set-key  [f4] 'previous-error)
(global-set-key  [f3] 'next-error)
(global-set-key  [f2] 'bookmark-set)
(global-set-key  [f8] 'bookmark-jump)
(global-set-key  [f12] 'tab-display-toggle)
(global-set-key  [(meta g)] 'goto-line)
(global-set-key  [(control c) (l)] 'wb-line-number-toggle)
;;(global-set-key  [(control c) (f)] 'semantic-ia-complete-symbol)

(global-font-lock-mode t)
(setq visible-bell t)
(display-time)
(transient-mark-mode t)
(show-paren-mode t)
(setq default-major-mode 'text-mode)
;;(setq show-paren-style 'parentheses)
(setq scroll-step 1
      scroll-margin 3
      scroll-conservatively 10000)
(setq frame-title-format "emacs@%b")

;;proxy
(setq url-proxy-services
   '(("no_proxy" . "^\\(localhost\\|10.*\\)")
     ("http" . "proxy-fm.intel.com:912")
     ("https" . "proxy-fm.intel.com:912")))
;; Configuration variables here:
;;(setq semantic-load-turn-useful-things-on t)
;; Load CEDET
;;(load-file "~/cedet-1-2b/common/cedet.el")
;;(require 'xcscope)
(add-to-list 'load-path "~/.emacs.d/cl-lib")
(require 'cl-lib)
(add-to-list 'load-path "~/.emacs.d/")



(require 'color-theme)
(color-theme-initialize)
(color-theme-matrix)
;;set default theme
(color-theme-dark-blue)
;;(require 'tab-display)
(set-scroll-bar-mode nil)
;;(require 'wb-line-number)
;;(wb-line-number-enable)
(tool-bar-mode -1)
(fset 'yes-or-no-p 'y-or-n-p)
(column-number-mode t)
(setq-default make-backup-files nil)
(setq kill-ring-max 200)

(defun linux-c-mode()
(interactive)
(c-mode)
(c-set-style "k&r")
(setq c-basic-offset 4)
(c-toggle-auto-state)
)
(setq auto-mode-alist(cons '("\\.[ch]\\'" . linux-c-mode)
auto-mode-alist))

(defun linux-c-mode()
(interactive)
(c-mode)
(c-set-style "k&r")
(setq c-basic-offset 4)
(c-toggle-auto-state)
)
(setq auto-mode-alist(cons '("\\.cpp\\'" . linux-c-mode)
auto-mode-alist))

(setq auto-mode-alist(cons '("\\.java\\'" . linux-c-mode)
auto-mode-alist))
;;for javascript
(autoload 'js2-mode "js2-mode" nil t)
(add-to-list 'auto-mode-alist '("\\.js$" . js2-mode))

;;refer a blog
;;(add-to-list 'load-path (expand-file-name "~/site-lisp/mmm-mode"))
(require 'php-mode)
(add-hook 'php-mode-user-hook 'turn-on-font-lock)
(require 'mmm-mode)
(setq mmm-global-mode 'maybe)
(setq c-basic-offset 4)
(mmm-add-group
'php-in-html
'(
(html-php-tagged
:submode php-mode
:front "<\?"
:back "\?>"
:include-back t)))
(add-hook 'html-mode-hook '(lambda ()
(setq mmm-classes '(php-in-html))
(set-face-background
'mmm-default-submode-face "Blank")
(mmm-mode-on)))
(add-to-list 'auto-mode-alist '("\.php[34]?\'" . html-mode))
(add-to-list 'mmm-mode-ext-classes-alist '(html-mode nil fancy-html))

;;????,????????
(load-library "hideshow")
(add-hook 'php-mode-hook 'hs-minor-mode)

(custom-set-variables
  ;; custom-set-variables was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 '(c-tab-always-indent t)
 '(case-fold-search t)
 '(column-number-mode t)
 '(current-language-environment "English")
 '(default-input-method "chinese-py-punct")
 '(display-time-mode t)
 '(global-font-lock-mode t nil (font-lock))
 '(indent-tabs-mode nil)
 '(safe-local-variable-values (quote ((sh-indentation . 2))))
 '(show-paren-mode t nil (paren))
 '(show-paren-style (quote mixed))
 '(transient-mark-mode t))
(custom-set-faces
  ;; custom-set-faces was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 )