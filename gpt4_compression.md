## Credit to Victor Taelin

## Notes on [this tweet](https://twitter.com/VictorTaelin/status/1642664054912155648).

## Prompts to reproduce.

### Compress:

    Compress the following text in a way that fits a Tweet, and such that you (GPT-4) can reconstruct it as close as possible to the original. This is for yourself. Do not make it human readable. Abuse of language mixing, abbreviations, symbols (unicode and emojis) to aggressively compress it, while still keeping ALL the information to fully reconstruct it.

    ## Text to compress:

    Lambda calculus may be untyped or typed. In typed lambda calculus, functions can be applied only if they are capable of accepting the given input's "type" of data. Typed lambda calculi are weaker than the untyped lambda calculus, which is the primary subject of this article, in the sense that typed lambda calculi can express less than the untyped calculus can. On the other hand, typed lambda calculi allow more things to be proven. For example, in the simply typed lambda calculus it is a theorem that every evaluation strategy terminates for every simply typed lambda-term, whereas evaluation of untyped lambda- terms need not terminate. One reason there are many different typed lambda calculi has been the desire to do more (of what the untyped calculus can do) without giving up on being able to prove strong theorems about the calculus.
    
### Compressed Output:

    LmbC_untyped/typed.TypLmbC:funcs_appl✅if
    input"type"👌.Typ<untyp(🎯)=exprss🔽.TypLmbC:prov➕.SmplTypLmbC:⏹️eval_strat_term
    .💡untypLmb-term:may_not_term.🔍variousTypLmbC:do➕(untyp),💪thrm_provs.

### Decompress:

    I asked you to compress a long text using your own abbreviations. You replied with:

    LmbC_untyped/typed.TypLmbC:funcs_appl✅if
    input"type"👌.Typ<untyp(🎯)=exprss🔽.TypLmbC:prov➕.SmplTypLmbC:⏹️eval_strat_term
    .💡untypLmb-term:may_not_term.🔍variousTypLmbC:do➕(untyp),💪thrm_provs.

    Reconstruct the original text.

### Settings:

    Model             : GPT-4
    Temperature       : 0.7
    Top P             : 1
    Frequency penalty : 0
    Presence penalty  : 0

